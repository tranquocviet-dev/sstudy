class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.__name = name
        self.__employee_id = employee_id
        self.__base_salary = base_salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new):
        self.__name = new

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def base_salary(self):
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, new):
        self.__base_salary = new

    def calculate_salary(self):
        print(f"salary is {self.base_salary}")


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, bonus):
        super().__init__(name, employee_id, base_salary)
        self.__bonus = bonus

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, new):
        self.__bonus = new

    def calculate_salary(self):
        print(f"salary is {self.base_salary + self.bonus}")


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id, 0)
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, new):
        self.__hours_worked = new

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, new):
        self.__hourly_rate = new

    def calculate_salary(self):
        print(f"slary is {self.hours_worked * self.hourly_rate}")


class Manager(FullTimeEmployee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id, 0, 0)
        self.__team_size = team_size

    @property
    def team_size(self):
        return self.__team_size

    @team_size.setter
    def team_size(self, new):
        self.__team_size = new

    def calculate_salary(self):
        print(f"salary is {self.team_size * 500000}")


if __name__ == "__main__":
    khang = Employee("Khang", 20, 100)
    khang.calculate_salary()
    duc = FullTimeEmployee("Duc", 21, 200, 50)
    duc.calculate_salary()
    viet = PartTimeEmployee("Viet", 22, 300, 50)
    viet.calculate_salary()
