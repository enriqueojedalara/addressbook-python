import logging
import hashlib
import time
import json
from addressbook.utils.web import HTTPError, AccessToken
from addressbook.models.main import (
    UserModel,
    BookModel,
)
from addressbook.utils.conf import settings

logger = logging.getLogger(__name__)

class BaseController(AccessToken) :
	def __init__(self):
		pass

	def validate_parameters(self, required, params):
		req_args = set(required).difference(params)
		if req_args:
			err = 'Following arguments are required: %s'
			raise HTTPError(400, err % (', '.join(req_args)))

	def initialize_fields_or_none(self, params, fields):
		for field in fields:
			params[field] = params.get(field, None)
		return params

	def create_access_token(self, user):
		return AccessToken.create(user)

	def validate_access_token(self, access_token):
		return AccessToken.validate(access_token)

	def load_access_token_data(self, access_token):
		return AccessToken.validate(access_token, True)


class UserController(BaseController):
	def __init__(self):
		BaseController.__init__(self)
		self.user_model = UserModel()

	def login(self, params):
		fields_required = ['email', 'passwd']
		self.validate_parameters(fields_required, params)
		params = self.initialize_fields_or_none(params, fields_required)
		
		user = self.user_model.login(params.get('email'))
		if not user:
			time.sleep(int(settings.delay_login_failure))
			raise HTTPError(404, 'User %s not found' % params.get('email'))
		user = user[0]

		passwd = hashlib.sha1(params.get('passwd')).hexdigest()
		if (str(passwd) != user.get('password')):
			time.sleep(int(settings.delay_login_failure))
			raise HTTPError(404, 'Incorrect password')

		#Avoid save password in access token
		try:
			del user['password']
		except:
			pass

		#Add delay if there is an error
		try:
			res = self.create_access_token(user)
		except:
			time.sleep(int(settings.delay_login_failure))
			raise
		return res


class BookController(BaseController):
	def __init__(self, access_token = None):
		BaseController.__init__(self)
		self.book_model = BookModel()
		if access_token != None:
			self.validate_access_token(access_token)

	def contacts(self, access_token):
		user = self.load_access_token_data(access_token)
		contacts = self.book_model.contacts(user.get('uid'))
		for (k, v) in enumerate(contacts):
			contacts[k]['details'] = self.book_model.load_custom_info(v.get('cid'))
		return json.dumps(contacts)
