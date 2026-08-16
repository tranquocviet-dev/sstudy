class Rectangle:
    def __init__(self, name:str, width:int, height:int, letter:str):
        self.__name = name[:4]
        self.__width = width
        self.__height = height
        self.letter = letter[0]
    @property
    def name(self):
        return self.__name
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    def show(self):
        print(f'Rectangle {self.name} ({self.width} x {self.height})')
    def draw(self):
        for i in range(self.height):
            for i in range(self.width):
                print(self.letter, end="")
            print("")
    def draw_empty(self):
        #first line
        for i in range(self.width):
            print(self.letter, end="")
        print("")
        #middle
        for i in range(self.height - 2):
            print(self.letter, end="")
            for i in range(self.width - 2): print(" ", end="")
            print(self.letter)
        #last line
        for i in range(self.width):
            print(self.letter, end="")
        print("")
    def draw_with_coord(self):
        coords = list(self.name)
        # first coords line
        print(f"{coords[0]}", end="")
        for i in range(self.width - 2): print(" ", end="")
        print(f"{coords[1]}")
        #main draw
        for i in range(self.height):
            for i in range(self.width):
                print(self.letter, end="")
            print("")
        # last coords line
        print(f"{coords[2]}", end="")
        for i in range(self.width - 2): print(" ", end="")
        print(f"{coords[3]}")

foo = Rectangle("ABCD", 7, 5, "*")
foo.show()
foo.draw()
print("")
foo.draw_empty()
print("")
foo.draw_with_coord()
bar = Rectangle("EFGH", 8, 6, "#")
bar.draw_with_coord()


# square
class Square(Rectangle):
    def __init__(self, name, size, letter):
        super().__init__(name, size, size, letter)

foobar = Square("IJKLM", 5, "^")
foobar.draw()
foobar.show()
