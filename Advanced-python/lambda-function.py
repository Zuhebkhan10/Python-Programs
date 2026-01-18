# lambda function: lambda function is an anonymous function(no name) where it takes
# many arguments and single expression.

# Expression:the step used to give a output know as expression
def num():
    return "Call me don"
print(num()) # lambda argument: single expression

b=lambda x,y,z :(x+15,y+10,z+18)
print(b(10,20,25))


c=lambda x,y:(x*2,y*5)
print(c(15,25))


# Function are the first class objects: A function can use like argument lambda is more powerful
# when we use inside the function.

# Write a program to print square ,cube,and sqrt
#Without using lambda function.
def square(n):
   return n**2
def cube(n):
    return n**3
def sqrt(n):
    return n**0.5

print(square(5))
print(cube(3))
print(sqrt(25))



def power(a):
    return lambda x:x**a
square=power(2)
cube=power(3)
sqrt=power(0.5)

print(square(6))
print(cube(2))
print(sqrt(49))





