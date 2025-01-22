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


class Manager(Employee):
    raise_amt = 1.20
    
    def __init__(self,first,last,pay,employees=None): #never pass [] mutable datatype, it will run once during fn defnand use it always
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay)
        if employees is None:
            self.employees + []
        else:
            self.employees = employees
        
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_emp(self):
        for emp in self.employees:
            print(f'*** {emp.fullname()}')

emp1=Employee('Akash','Raina',12020)
emp2=Employee('Bavana','Patel',11211)
man1=Manager('Shilpa','Shetty',550000,[emp1])
man1.add_emp(emp2)
man1.print_emp()

#print(help(Manager))

print(isinstance(man1,Manager))
print(isinstance(man1,Employee))
print(issubclass(Manager,Employee))