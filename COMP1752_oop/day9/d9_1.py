class Account():
	def __init__(self, name):
		self.__owner = name
		self.__balance = 0
	@property
	def owner(self):
		return self.__owner
	@owner.setter
	def owner(self, new):
		if new == '':
			raise ValueError('Owner can not be empty')
		else:
			self.__owner = new
	def deposit(self, num)

class bank:
	def __init__(self):
	def create_account(self):
		acc_type = input('')

class with_uuid(self)
class account(with_uuid):
	def __init__(self, name):
		self.name = name
		uuid.append(name)
		self.uuid = list.index(name)
		self.__balance = 0
