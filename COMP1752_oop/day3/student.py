class Student:
    def __init__(self, name, age, grade):
        self.__name = name
        self.__age = age
        self.grade = grade

    def show(self):
        print(f'Student: {self.__name}, Age: {self.__age}, Grade: {self.__grade}')

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name == '':
            print('Name cant be empty')
        else:
            self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age == '':
            print('Age cant be empty')
        else:
            self.__age = age

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if grade.upper not in ['A', 'B', 'C', 'D', 'F']:
            print('Grade invalid')
        else:
            self.__grade = grade.upper
