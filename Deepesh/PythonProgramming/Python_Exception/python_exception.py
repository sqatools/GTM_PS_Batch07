# initiate the except handling and provide custom msg
def handle_exception_with_msg():
    try:
        num1 = 10
        num2 = 'Hello'

        print(num1 + num2)
    except Exception as e:
        print(e)
        print("Can not add number with string")


# handle_exception_with_msg()
# print("Good morning")


# raise the exception explicitly and fail the program
def raised_exception(num1, num2):
    try:
        division = num1 // num2
        print("division num1 and num2 :", division)
    except Exception as e:
        print("Division is not successful")
        raise e


# raised_exception(25, 0)  # raise a exception msg (ZeroDivisionError: integer division or modulo by zero)
# print("Good morning")
# raised_exception(25, 5)
print("Good morning")


##### try-except- else condition  ######
# else block only executes when there is no exception in our code

def try_except_else(num1, num2, num3):
    try:
        add = num1 + num2
        print("addition :", add)
        print("division :", num2 / num3)
    except Exception as e:
        print("Failed with error")
        print(e)
    else:
        print("Execution of the code is successful")


# try_except_else(20, 5, 6)  # else block will execute

# if there is exception in the code then else block will not execute
# try_except_else(20, '5', 0) # unsupported operand type(s) for +: 'int' and 'str'


###### Try-except-else-finally ######
# finally-block always execute the code, even there is exception or no exception.

def try_except_else_finally(num1, num2, num3):
    try:
        add = num1 + num2
        print("addition :", add)
        print("division :", num2 / num3)
    except Exception as e:
        print("Failed with error")
        print(e)
    else:
        # else is optional block, we can add/remove as per requirement
        print("Execution of the code is successful")
    finally:
        # finally is optional block, we can add/remove as per requirement
        print("Table of number : ", num1)
        for i in range(1, 11):
            print(i, "*", num1, ":", i * num1)


# case1 : No exception : All the block will execute successfully
# try_except_else_finally(10, 5, 3)

# case2 : Error in code :  If the exception occure, then else block will not execute, and
# finally block will still execute and provide output
# try_except_else_finally(7, '5', 3)

# We can use the finally block without else block as well, it is not compulsory to use else block
# along with finally block.


############# Handle multiple excpetion in one program #######

def handle_multiple_exception(num1, num2, num3, filename):
    try:

        print("addition :", num1 + num2)
        print("division :", num2 / num3)
        # read file content
        with open(filename, "r") as file:
            data = file.read()
            print(data)
    except TypeError:
        print("Both the number should be integer")
    except ZeroDivisionError:
        print("Can not divide the number with Zero")
    except FileNotFoundError:
        print("Can not find specified file locally :", filename)
    except Exception as e:
        print("Failed with error")
        raise e


# case 1: No exception
# handle_multiple_exception(20, 10, 5, "data_file.txt")

# case 2 : failed in addition
# handle_multiple_exception(20, '7', 5, "data_file.txt")

# case 3 : failed in division
# handle_multiple_exception(20, 10, 0, "data_file.txt")

# case 3 : read invalid file
# handle_multiple_exception(20, 10, 2, "data_file_2.txt")


############# Nested level exception ###############

def multi_level_exception(num1, num2, num3):
    try:
        print("addition :", num1 + num2)
        try:
            print("division :", num2 / num3)
        except Exception as e:
            print(e)
            print("Can not divide the number with zero")

    except Exception as e:
        print(e)
        print("Both the value should be integer")


# case 1 :  outer exception
# multi_level_exception(40, 'Python', 30)

# case 3 :  inner exception
# multi_level_exception(40, 4, 0)


############# custom exception ##############

class MyException(Exception):
    pass


def use_custom_exception():
    for i in range(1, 20):
        print(i)
        if i == 7:
            raise MyException("This number is not allowed")


use_custom_exception()
