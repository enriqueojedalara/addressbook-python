import logging
from addressbook.utils.conf import settings
from addressbook.utils.db.mysql import Mysql


logger = logging.getLogger(__name__)

class BaseModel:
	def __init__(self):
		self.db = Mysql(host=settings.dbhost, 
						user=settings.dbuser,
						passwd=settings.dbpasswd,
						db=settings.dbname,
						port=int(settings.dbport),
						charset=settings.dbcharset)

class UserModel(BaseModel):
	def __init__(self):
		BaseModel.__init__(self)

	def login(self, email):
		sql = ('SELECT `uid`, `name`, `mobile`, `email`, `password` '
			   'FROM `users` '
			   'WHERE `email` = %s ')
		return self.db.execute(sql, email)


class BookModel(BaseModel):
	def __init__(self):
		BaseModel.__init__(self)

	def contacts(self, user_uid):
		sql = ('SELECT `cid`, `name`, `lastname`, `picture`, `address` '
			   'FROM `contacts` '
			   'WHERE `uid` = %s '
			   'ORDER BY `name` ASC ')
		return self.db.execute(sql, user_uid)

	def load_custom_info(self, cid):
		return {
			'emails': self.contact_emails(cid),
			'phones': self.contact_phones(cid),
			'sn': self.contact_social_networks(cid),
			'custom': self.contact_custom_fields(cid)
		}

	def contact_emails(self, cid):
		sql = ('SELECT `id`, `email`, `type` '
			   'FROM `emails` '
			   'WHERE `cid` = %s '
			   'ORDER BY `id` ASC ')
		return self.db.execute(sql, cid)

	def contact_phones(self, cid):
		sql = ('SELECT `id`, `phone`, `type` '
			   'FROM `phones` '
			   'WHERE `cid` = %s '
			   'ORDER BY `id` ASC ')
		return self.db.execute(sql, cid)

	def contact_social_networks(self, cid):
		sql = ('SELECT `snid`, `name`, `username`, `url` '
			   'FROM `contact_sn` csn JOIN `social_networks` sn ON (csn.snid = sn.id) '
			   'WHERE `cid` = %s ')
		return self.db.execute(sql, cid)

	def contact_custom_fields(self, cid):
		sql = ('SELECT `id`, `field`, `value` '
			   'FROM `custom_fields` '
			   'WHERE `cid` = %s ')
		return self.db.execute(sql, cid)