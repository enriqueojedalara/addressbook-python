from collections import defaultdict

class Settings:
	'''Settings is an observable key-value object accessible by attribute'''
	def __init__(self, *args):
		self.__dict__['settings'] = {}
		for settings in args:
			self.add(settings)

	def update(self, *args, **kwargs):
		self.settings.update(*args, **kwargs)

	def __setattr__(self, name, value):
		self.settings[name] = value
		for callback in self.observers[name]:
			callback(value)

	def __getattr__(self, name):
		return self.settings[name]

	def get(self, *args, **kwargs):
		return self.settings.get(*args, **kwargs)

	def __str__(self, name):
		pass


#Singleton instance
settings = Settings()