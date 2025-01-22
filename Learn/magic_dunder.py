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

    def __repr__(self):
        return f"Employee('{self.first}','{self.last}','{self.pay})"

    def __str__(self):
        return f"'{self.fullname()}' - '{self.email}'"
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.first)

emp1=Employee('Baba','Ramdev',12345)
print(repr(emp1))
print(emp1)

emp2 = Employee('amit','Rana',22112)

print(emp1 + emp2)

print(len('key'))
print('key'.__len__())

print(len(emp1))