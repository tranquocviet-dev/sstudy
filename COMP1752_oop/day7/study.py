PI = 3.14

class Shape():
	def __init__(self, name, type):
		self.__name = name
		self.type = type

	@property
	def area(self):
		return self.__area

	def __str__(self):
		return(f"{self.type} {self.__name} area {self.area} m2")

class Rectangle(Shape):
	def __init__(self, name, width, height):
		super().__init__(name, "Rectangle")

		self.__width = width
		self.__height = height

	@property
	def width(self):
		return self.__width

	@property
	def height(self):
		return self.__height

	@property
	def area(self):
		return self.__width * self.__height

class Triangle(Shape):
	def __init__(self, name, a, b, c):
		super().__init__(name, "Triangle")
		self.__a = a
		self.__b = b
		self.__c = c

	@property
	def a(self):
		return self.__a

	@property
	def b(self):
		return self.__b

	@property
	def c(self):
		return self.__c

	@property
	def area(self):
		p = (self.__a + self.__b + self.__c) / 2
		s = (p * (p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5 
		return s

class IsoTriangle(Triangle):
	def __init__(self, name, base, side):
		super().__init__(name, base, side, side)
		self.type = "Isosceles Triangle"

	@property
	def side(self):
		return self.c

	@property
	def base(self):
		return self.a

class EqTriangle(Triangle):
	def __init__ (self, name, side):
		super().__init__(name, side, side, side)
		self.type = "Equal Triangle"

	@property
	def side(self):
		return self.a

class Eclipse(Shape):
	def __init__(self, name, rw, rh):
		super().__init__(name, "Eclipse")
		self.__rw = rw
		self.__rh = rh

	@property
	def rw(self):
		return self.__rw

	@property
	def rh(self):
		return self.__rh

	@property
	def area(self):
		return self.__rw * self.__rh * PI

class Circle(Eclipse):
	def __init__(self, name, r):
		super().__init__(name, r, r)
		self.type = "Circle"

	@property
	def r(self):
		return self.r

if __name__ == "__main__":
	rect = Rectangle("ABCD", 5, 10)
	print(rect)
	tri = Triangle("ABC", 3, 4, 5)
	print(tri)
	itri = IsoTriangle("ABC", 3, 5)
	print(itri)
	etri = EqTriangle("ABC", 5)
	print(etri)
	ecl = Eclipse("A", 4, 6)
	print(ecl)
	cir = Circle("B", 5)
	print(cir)
