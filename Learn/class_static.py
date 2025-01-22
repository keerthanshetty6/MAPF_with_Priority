class Employee:
    num_of_employees=0
    raise_amt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@email.com'

    def fullname(self):
        return f'Full Name {self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amt):
        cls.raise_amt=amt
    #Alternative Constructors
    @classmethod
    def from_String(cls,str):
        first,last,pay = str.split('-')
        return cls(first,last,pay) # calls class init
    
    @staticmethod
    def workday(day):
        if day.weekday() >= 5:
            return False
        return True

emp1=Employee('Anil', 'Shetty', 50000)
emp2=Employee('Sunil', 'Shetty',10000)
emp_Str='Keerthan-Shetty-20000'


print(emp1.fullname(),emp1.raise_amt)
print(emp2.fullname(),emp2.raise_amt)
print(Employee.raise_amt)
emp1.raise_amt=1.10
print(emp1.fullname(),emp1.raise_amt)
print(emp2.fullname(),emp2.raise_amt)

emp1.set_raise_amt(1.05)
print(emp1.fullname(),emp1.raise_amt)
print(emp2.fullname(),emp2.raise_amt)
print(Employee.raise_amt)
emp3=Employee.from_String(emp_Str)
print(emp3.email,emp3.pay)

class Animal:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_with_name(cls, name):
        return cls(name)

class Dog(Animal):
    pass

# Using the class method
animal = Animal.create_with_name("Generic Animal")
dog = Dog.create_with_name("Buddy")

print(type(animal))  # <class '__main__.Animal'>
print(type(dog))     # <class '__main__.Dog'>


import datetime
day = datetime.date(2025,4,26)
print(Employee.workday(day))