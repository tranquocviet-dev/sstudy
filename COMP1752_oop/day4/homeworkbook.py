class Book:
    def __init__(self, isbn:str, title:str, author:str, price:int, copies:int):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__price = price
        self.__copies = copies

    @property
    def isbn(self):
        return self.__isbn

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new):
        if new == '':
            print("cant be empty")
            return
        else:
            self.__title = new

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

    def borrow_book(self, qty):
        if qty > self.__copies:
            print('not enough copies to borrow')
            return
        if qty < 1:
            print('cant borrow less than 1 books')
            return
        else:
            print(f'borrowing {qty} books.')
            self.__copies -= qty

    def return_book(self, quantity):
        if quantity < 1:
            print('cant return less than 1 books')
            return
        else:
            print(f'returning {quantity} books.')
            self.__copies += quantity

if __name__ == "__main__":
    dune = Book("0441172719", "dune", "Frank Herbert", 20, 300)
    print(f'CALLING THE GET PROPERTIES')
    print(dune.isbn)
    print(dune.title)
    print(dune.author)
    print(dune.price)

    print(f'CALLING THE SET PROPERTIES')
    dune.title = "Dune Part 1"
    dune.price = 25
    print(dune.title)
    print(dune.price)

    print(f'CALLING THE BORROW AND RETURN FUNCTION')
    dune.borrow_book(400)
    dune.borrow_book(-30)
    dune.borrow_book(20)

    dune.return_book(-30)
    dune.return_book(20)
