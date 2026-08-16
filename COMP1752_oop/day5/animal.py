class Animal:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    def speak(self):
        print(f'The animal {self.name} aged {self.age} is saying something, never to be understood')

class Pet(Animal):
    def __init__(self, name:str, age:int, owner:str):
        super().__init__(name, age)
        self.owner = owner

    def speak(self):
        print(f'{self.owner}s pet {self.name} aged {self.age} is saying something. {self.owner} pretend to understand')


if __name__ == "__main__":
    dog = Animal("some random dog", 2)
    dog.speak()
    hus = Pet("Huski Doggie", 2, "Viet")
    hus.speak()
