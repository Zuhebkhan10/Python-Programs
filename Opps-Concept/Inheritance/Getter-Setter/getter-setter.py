# A getter is a method used to get (read) the value of a variable.
# A setter is a method used to set (update) the value of a variable.


# Why do we need Getters and Setters?
# Instead of accessing variables directly, getters and setters help to:
# Protect data (data encapsulation)
# Validate values before setting them
# Control how values are read or changed
# Make your code safer and cleaner

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @property
    def first_name(self):
        l=self.name.split(" ")
        return l[0]

    @first_name.setter
    def first_name(self,first):
        l=self.name.split(" ")

        new_name=f"{first} {l[1]}"
        self.name=new_name

e=Employee("Sarim khan",89311)
# print(e.first_name())
#
# e.set_first_name("shahzain")
# print(e.name)

print(e.first_name)
e.first_name="Aazil"
print(e.name)