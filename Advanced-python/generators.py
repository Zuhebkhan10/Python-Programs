 # Generators: returns the value one at a time and saves the memory when we
 # create generate we use "Yield" instead of "return"

def hello():
    return 10
    return 20
    return 30
# print(hello())
# print(hello())
# print(hello())


def f1():
    return 10
    return 20
    return 30
# print(f1())

def func():
    yield 30
    yield 40
    yield 50
# print(func())
gen=func()
print(next(gen))
print(next(gen))
print(next(gen))

def p1():
    return [1,2,3,4]
print(p1())

num