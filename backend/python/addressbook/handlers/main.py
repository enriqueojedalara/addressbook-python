import tornado.web
import datetime
import logging
from addressbook.utils.web import (
    RequestHandler,
    web_adaptor
)
from addressbook.controllers.main import (
    UserController,
    BookController,
)
from addressbook.utils.conf import settings

logger = logging.getLogger(__name__)


class UserHandler(RequestHandler):
    @web_adaptor
    def post(self, *args, **kwargs):
        self.validate_content_type()
        params = self.get_http_body()
        self.finish(UserController().login(params))


class BookHandler(RequestHandler):
    @web_adaptor
    def get(self, *args, **kwargs):
        access_token = self.get_access_token()
        self.finish(BookController().contacts(access_token))


class NotFoundErrorHandler(RequestHandler):
    @web_adaptor
    def get(self, *args,  **kwargs):
        error = {
            "code": 404,
            "message":"HTTP Request was not found"
        }
        self.set_status(error['code'])
        self.write(error)
        self.finish()


