import logging
import datetime


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
            self.write({'error': e.body})
    return decorated
