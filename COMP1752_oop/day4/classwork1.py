class Item:
	def __init__(self, proid:int, name:str, price:int, quantity:int):
		self.__proid = proid
		self.__name = name
		self.__price = price
		self.__quantity = quantity

	@property
	def proid(self):
		return self.__proid

	@property
	def price(self):
		return self.__price

	@price.setter
	def price(self, new):
		if new < 0:
			print("cant be below 0")
			return
		else:
			self.__price = new

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, new):
		if new == '':
			print("cant be empty")
			return
		else:
			self.__name = new

	def add_amount(self, add):
		if add < 0:
			print("amount cant be below 0")
			return
		else:
			self.__price += add

	def decrease_amount(self, decrease):
		if decrease < 0:
			print("amount cant be below 0")
			return
		elif decrease >= self.__price:
			print('cant decrease if end price is below or equal to 0')
		else:
			self.__price -= decrease

	def get(self):
		print(f'The product {self.__name} has index {self.__proid} with price {self.__price} is {self.__quality}')

if __name__ == "__main__":
	trash = Item(10, "pen", 5, 10)
	pen = Item(10, "pen", 5, 20)
	pen.name = ''
	pen.name = 'pencil'
	pen.price = -1
	pen.price = 4
	pen.get()
	pen.add_amount(-1)
	pen.add_amount(2)
	pen.decrease_amount(-1)
	pen.decrease_amount(9)
	pen.decrease_amount(2)
	pen.get()
