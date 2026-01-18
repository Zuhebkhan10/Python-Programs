# Decorator is a function that takes a function it creates a new function inside its body (wrapper)
# then it returns that new function.
def decorator(func):
    def wrapper():
        print("I am about to execute a function")
        func()
        print("I have executed this function")
    return wrapper

@decorator
def say():
    print("Done")

say()

# s=decorator(say)
# s()

