# Simple demo remote
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Use property
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

    def get(self):
        print(f'Student {self.__name} age {self.age}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new):
        if new < 0:
            print("cant be below 0")
            return
        else:
            self.__age = new

if __name__ == "__main__":
    khang = Student('Khang', 19)
    print(f'{khang.name}')
    khang.name = ''
    khang.name = 'Khang ko Gay'
    print(f'{khang.name}')
    print(khang.age)
    khang.age = -1
    khang.age = 18
    print(khang.age)
    print(khang.name, khang.age)
    khang.get()
