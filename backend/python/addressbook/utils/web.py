import logging
import datetime
import base64
import json
import time
import tornado
from Crypto.Cipher import AES

logger = logging.getLogger(__name__)


class HTTPError(Exception):
    """Custom HTTPError class
    """
    def __init__(self, status, body, show=False):
        try:
            json = json.loads(body)
            if 'error' in json:
                body = json['error']
        except:
            pass
        Exception.__init__(self, '%s - %s' % (status, body))
        self.status, self.body, self.show = status, body, show
        logger.error('Error %s: %s' % (status, body))


class RequestHandler(tornado.web.RequestHandler):

    VALIDATE_JSON_HEADERS = ['application/json', 'application/json; charset=UTF-8']

    def validate_content_type(self):
        for header in self.VALIDATE_JSON_HEADERS:
            if self.request.headers.get('Content-Type').lower().strip().startswith(header): 
                return True
        msg = 'This service only speaks %s, check if you have the correct header, you sent %s'
        raise HTTPError(400, msg % (self.VALIDATE_JSON_HEADERS[0], self.request.headers.get('Content-Type')))

    def get_http_body(self):
        try:
            params = tornado.escape.json_decode(self.request.body)
        except:
            raise HTTPError(400, 'Parameter in HTTP body is not a valid JSON')
        return params

    def get_access_token(self):
        if self.request.headers.get('Authorization') is None:
            raise HTTPError(401, 'Authorization is required')
        return self.request.headers.get('Authorization')


def web_adaptor(f):
    """Decorator that add the HTTP response and set the format to all HTTP responses
    """
    def decorated(self, *args, **kwargs):
        try:
            self.set_header("Content-Type", 'application/json')
            self.set_header('Date', datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT"))
            kwargs.update(dict((k, values[-1]) for k, values in self.request.arguments.items()))
            return f(self, *args, **kwargs)
        except HTTPError, e:
            self.set_status(e.status)
            self.write({'code': e.status, 'error': e.body})
    return decorated



class AccessToken:

    PRIVATE_KEY="Compu-Global-Hyper-Mega-Net-From-Homer-Simpson"
    DEFAULT_TIME_LIFE = 24*60*60

    @staticmethod
    def create(s):
        s['expire'] = time.time() + AccessToken.DEFAULT_TIME_LIFE
        s = json.dumps(s)
        secret = AES.new(AccessToken.PRIVATE_KEY[:32])
        string = (str(s) + (AES.block_size - len(str(s)) % AES.block_size) * "\0")
        access_token = base64.b64encode(secret.encrypt(string))
        return {"access_token": access_token}

    @staticmethod
    def validate(s, data = False):
        try:
            secret = AES.new(AccessToken.PRIVATE_KEY[:32])
            decrypted = secret.decrypt(base64.b64decode(s))
            access_token = decrypted.rstrip("\0")
            s = json.loads(access_token)
        except:
            raise HTTPError(401, 'Invalid access token %s' % s)
        if s.get('expire') < time.time():
            raise HTTPError(401, 'Access token has expired')
        if data:
            return s
        return True
