"""
Constructors:The __init__ method is special. It's called the constructor. It's automatically run whenever you
create a new object from a class.

The constructor's job is to initialize the object's attributes – to give them their starting values. It sets up
the initial state of the object.

"""
class Employee:

    def __init__(self,name,salary,bond):
        self.name=name
        self.salary=salary
        self.bond=bond

    def get_salary(self):
        return self.name

    def get_info(self):
        print(f"The name of the employee {self.name} salary is {self.salary} and the bond is for {self.bond} years")

e=Employee("Emma",45000,5)
# print(e.get_salary())
e.get_info()
