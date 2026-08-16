class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def greet(self):
        return f"Hello my name is {self.name} and I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, sid):
        super().__init__(name, age)
        self.__student_id = sid

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

    def greet(self):
        super().greet()
        print(
            f"i am a student with name {self.name}, age {self.age} and student id {self.student_id}"
        )


khang = Student("khang gay", 20, "gg123")
khang.greet()
