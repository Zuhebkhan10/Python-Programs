"""Instance Attributes: These are specific to each individual object. name and breed are instance attributes.
Each dog has its own name and breed. They are usually defined within the __init__ method.

Class Attributes: These are shared by all objects of the class. Like species in our Dog class. All dogs belong
to the same species.They are defined outside  any method, directly within the class.
"""

class Employee:
    company="Amazon" #This is class attribute

    def __init__(self,name,salary,bond,company):
        self.name=name
        self.salary=salary
        self.bond=bond
        self.company=company

    def get_salary(self):
        return self.salary

    def get_info(self):
        return (f"The name of employee the {self.name} salary is {self.salary} and the bond is for {self.bond} years")

e=Employee("Duffy",55500,4,"Oracle")
print(e.get_info())
print(e.get_salary())

print(e.company)#Will always print instance attribute whenever present
print(Employee.company)# This will always print the class attributes

#Objetc introspection
print(dir(e))