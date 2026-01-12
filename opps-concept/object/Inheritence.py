"""
Inheritance is like a family tree. A child class (or subclass) inherits traits
(attributes and methods) from its parent class (or superclass). This allows you
to create new classes that are specialized versions ofexisting classes, without
rewriting all the code."""


class Animal:  #Parent class (Superclass)
    location="Hyedrabad"

    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Please speaking now")

class Cat(Animal):# This is how  inheritance is done in python
    def speak(self):
        super().speak() #We are using the speak function of the parent class
        print("Meow Meow meow")

a=Animal("Cat")
# a.speak()
print(a.location)

c=Cat("Maxii")
c.speak()

# print(c.location)
