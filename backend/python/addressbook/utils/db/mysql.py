import MySQLdb
import logging
import contextlib

logger = logging.getLogger(__name__)

class Mysql:
	
	conn = None
	cur = None
	conf = None

	def __init__(self, **kwargs):
		if 'charset' not in kwargs:
			kwargs['charset'] = 'utf8'
		if 'port' not in kwargs:
			kwargs['port'] = 3306
		self.conf = kwargs
		self.connect()

	def connect(self, **kwargs):
		try:
			if kwargs:
				self.conf = kwargs
			self.conn = MySQLdb.connect(**self.conf)
			self.cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
			self.conn.autocommit(True)
		except MySQLdb.Error as e:
			error = '%d. %s' % (e.args[0], e.args[1])
			logger.error('Error connecting with Mysql DBMS %s' % error)
			raise

	def execute(self, sql, *args, **kwargs):
		try:
			self.check()
			self.cur.execute(sql, args)
			if sql.lower().lstrip().startswith('select'):
				res = self.cur.fetchall()
			elif sql.lower().lstrip().startswith('insert'):
				res = self.cur.lastrowid
		except MySQLdb.Error as e:
			error = '%d. %s' % (e.args[0], e.args[1])
			logger.error('Error executing query "%s" => %s' % (sql, error))
			raise
		except Exception, e:
			logger.error('Error executing query %s' % e)
			self.conn.close()
			raise
		return res

	def check(self):
		try:
			self.conn.ping()
		except:
			self.connect()