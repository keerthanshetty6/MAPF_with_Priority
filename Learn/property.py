class Employee:
    num_of_employees=0
    raise_amt=1.04

    def __init__(self,first,last):
        self.first=first
        self.last = last
        
    @property # no need of () 
    def email(self):
        return self.first + '.' + self.last +'@email.com'
    @property
    def fullname(self):
        return f'Full Name {self.first} {self.last}'
    
    @fullname.setter
    def fullname(self,name):
        self.first,self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print(f'Deleting {self.first,self.last}')
        self.first,self.last = None,None
    
emp1 = Employee('Will','Smith')
print(emp1.fullname)
print(emp1.email)

emp1.first = 'Steve'
print(emp1.email)

emp1.fullname = 'Jared Dravid'
print(emp1.email)

del(emp1.fullname)
print(emp1)