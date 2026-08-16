class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new):
        if new < 0:
            print("cant be below 0")
            return
        else:
            self.__width = new

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new):
        if new < 0:
            print("cant be below 0")
            return
        else:
            self.__height = new

    def show(self):
        print(f'the rectangle is {self.__width}x{self.__height} with area {self.area}')

    @property
    def area(self): #without a setter the property is read only
        return self.__width * self.__height

if __name__ == "__main__": 
    rec = Rectangle(2, 4)
    rec.show()
    rec.width = -30
    rec.width = 5
    print(rec.width)
    rec.height = -30
    rec.height = 5
    print(rec.height)
    rec.show()
