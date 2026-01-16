class Customer:
    company="Amazon"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"

    def __repr__(self):
        return f"name:{self.name}\nsalary:{self.salary}"

    def __len__(self):
        return len(self.name)

c=Customer("Harry-Potter",56499)
print(c.name,c.salary)

# Print the ste function is customer c
print(str(c))

# print the repr function
print(repr(c))

print(len(c))