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
    print("multiplication :", num1*num2)


# call function with default value
multiplication(5)  # multiplication : 150

# call function and overwrite the default value
multiplication(7, 8) # multiplication : 56

# if we call function without providing the values, then it will through error
# multiplication()
# multiplication() missing 1 required positional argument: 'num1'




print("_"*50)
############################################
# provide expected data type to the function parameters

def add_values(v1: str, v2:str, v3:str):
    print("add result :", v1+v2+v3)


# python function gives warning if we don't provide the required data type
add_values(20, 30, 40)
# add result : 90

add_values('Hello ', 'Good ', 'Morning')
# add result : Hello Good Morning
