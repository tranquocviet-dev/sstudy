class Car:
    def __init__(self, brand:str, model:str, price):
        self.__brand = brand
        self.__model = model
        self.__price = price

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        if brand == '':
            print('brand cant be empty')
        else:
            self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        if model == '':
            print('model cant be empty')
        else:
            self.__model = model

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price <= 0:
            print('price cant be lower or equal to 0')
        else:
            self.__price = price

test = Car('abc', 'bcd', 9)
