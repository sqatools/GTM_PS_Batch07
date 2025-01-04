# function without parameter
def greeting():
    print("Good Morning")


# call function
greeting()
greeting()
greeting()
greeting()

print("_" * 50)


# function with parameter
def greeting_msg(msg):
    print(msg)


# There are two-way to provide value for paramter
# 1. pass by value
greeting_msg("Have a nice day")

# 2. Pass by reference
var1 = "Good Evening, Hope your are doing good."
greeting_msg(var1)

print("_" * 50)


# function with multiple parameters
def addition(n1, n2, n3):
    print("addition of values :", n1 + n2 + n3)


# pass by value
addition(30, 40, 50)
# addition of values : 120

# pass by value
x, y, z = 100, 200, 500
addition(x, y, z)
# addition of values : 800


###############################################
# function with default parameter value
"""
->  default parameter always comes at end of parameter list.
->  while calling function no need to pass value for default parameter, it will use the default value
->  If we provide value for default parameter while calling the function, then it
    will overwrite the default value
->  If we call function without providing the parameter value, then it will through error.
->  All parameters in the function can have default value.

"""


def multiplication(num1, num2=30):
    print("multiplication :", num1 * num2)


# call function with default value
multiplication(5)  # multiplication : 150

# call function and overwrite the default value
multiplication(7, 8)  # multiplication : 56

# if we call function without providing the values, then it will through error
# multiplication()
# multiplication() missing 1 required positional argument: 'num1'


print("_" * 50)


############################################
# provide expected data type to the function parameters

def add_values(v1: str, v2: str, v3: str):
    print("add result :", v1 + v2 + v3)


# python function gives warning if we don't provide the required data type
add_values(20, 30, 40)
# add result : 90

add_values('Hello ', 'Good ', 'Morning')
# add result : Hello Good Morning


print("_" * 50)


###########################################
# *args function parameter

def get_sum_of_all_value(*args):
    print(args)
    sum_value = 0
    for val in args:
        sum_value += val

    print("sum of all values :", sum_value)


get_sum_of_all_value(4, 5, 7, 2, 8, 11, 45)


def get_all_values(*args):
    print(args)
    sum_value = 0
    for val in args:
        print(val)


get_all_values(3, 3.4, 'Hello', [3, 5, 7], (33, 22, 11), {'a': 123, 'b': 345})

"""
3
3.4
Hello
[3, 5, 7]
(33, 22, 11)
{'a': 123, 'b': 345}
"""

print("_" * 50)


########################
# **kwargs parameter : This parameter accept the values in form of dictionary.

def get_user_details(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, ":", v)


get_user_details(name='john', email='john@gmail.com', address='Mumbai, boravali', phone=7878979)


def login(**kwargs):
    db_user = 'user1'
    db_pass = 'admin@12345'

    if kwargs['username'] == db_user and kwargs['password'] == db_pass:
        print("Login Successful")
    else:
        print("Access Denied wrong username password")


# login(username='user1', password='admin@12345')
login(username='user2', password='admin@12345')


############################################################
# function return value

def get_sum_of_values():
    sum_value = 0
    for i in range(20):
        print(i)
        sum_value += i
        if i == 10:
            return sum_value


result = get_sum_of_values()
print("addition result :", result)

print("_" * 50)


###################################
# return multiple values from function

def math_operation(n1, n2, n3):
    add = n1 + n2
    multi = n2 * n3
    subtract = n3 - n1
    return add, multi, subtract


output = math_operation(40, 50, 60)
print(output)  # (90, 3000, 20)

a, b, c = math_operation(5, 6, 7)
print("Addition value :", a)
print("Multiplication value :", b)
print("Subtraction value :", c)


#################################################
# call function inside function
# create a calculator to call the function inside function
def addition(n1, n2):
    return n1 + n2


def multiplication(n1, n2):
    return n1 * n2


def subtraction(n1, n2):
    return n1 - n2


def division(n1, n2):
    return n1 // n2


def calculator(num1, num2, operation):
    if operation == "+":
        print("addition of value :", addition(num1, num2))
    elif operation == "*":
        print("multiplication of value :", multiplication(num1, num2))
    elif operation == "-":
        print("subtraction of value :", subtraction(num1, num2))
    elif operation == "//":
        print("Division of value :", division(num1, num2))

print("_"*50)
calculator(20, 30, "+")
calculator(40, 30, "*")
calculator(5000, 30, "//")
calculator(400, 30, "-")

"""
addition of value : 50
multiplication of value : 1200
Division of value : 166
subtraction of value : 370
"""
