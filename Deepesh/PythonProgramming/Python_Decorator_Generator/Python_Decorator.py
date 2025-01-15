# decorator : decorator enhance the experience of the code without changing its existing functionality.

def decorator(func):
    def inner(*args):
        print("*"*30)
        func(*args)
        print("*"*30)
    return inner


@decorator
def greeting(msg):
    print(msg)

#greeting("Have a nice day")


@decorator
def factorial(n):
    fact =1
    for i in range(n, 0, -1):
        fact = fact * i

    print(f"Factorial of {n} :", fact)

factorial(6)


