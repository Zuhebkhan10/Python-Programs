"""
Polymorphism:
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators
with the same name that can be executed on many objects or classes.
"""

# function polymorphism

# String len(): For strings len() returns the number of characters:
a="Hello poly"
# print(len(a))


# tuple len(): For tuples len() returns the number of items in the tuple:
tuple=("Faiz","Kaif","Saif")
# print(len(tuple))


# dictionary :For dictionaries len() returns the number of key/value pairs in the dictionary:
info={
    "name":"Zuheb",
    "age":"21",
    "batch":"10 to 11",
    "course":"Data science",
    "Address":"Begumpet"
}
# print(len(info))



class Car:
    def __init__(self,brand,model):
      self.brand=brand
      self.model=model

    def move(self):
        print("Start drive.I am ready")


class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Sail.Could you please stop the boat I am feeling not well")

class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Yes. I am ready to Fly in the sky")


c=Car("BMW","M72") # create a car object
b=Boat("Ibiza","Touring-20") #create a Boat object
p=Plane("Boeing","747") # create a Plane object

# for x in (c,b,p):
#     x.move()

# c.move()
# b.move()
p.move()


