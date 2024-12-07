# 1.  Python Program to add two integer values.
'''
a = 15
b = 12

print(a+b)

# 2. Python Program to subtract two integer values.

print(a-b)

# 3). Python program to multiply two numbers.

print(a*b)

# 4). Python program to repeat a given string 5 times.

# Input :
str1 = "SQATools"
print(str1*5)

# 5).Python program to get the Average of given numbers.
c=11
print((a+b+c)/3)
'''
print ("_"*50)
'''
# 1). Python program to check given number is divided by 3 or not.

x = input("Enter the input value:")
x = int(x)
if x%3 == 0 :
    print(" This value is divisible by 3")
else :
    print("This value is not divisible by 3")
'''

# 4). Python program to check the given number divided by 3 and 5.
'''
x = input ("Enter the input value:")
x = int(x)
if x%3 == 0 and x%5 == 0:
    print ("The number is divided by 3 and 5")
else:
    print ("The number is not divided by 3 and 5")

'''
'''
# 5). Python program to print the square of the number if it is divided by 11.
x = input ("Enter the input value:")
x = int(x)
if x%11 == 0:
    print("The square of the number is: ", x**2)
else :
    print ("The number is not divisible by 11")
'''
# 7). Python program to check given number is odd or even.
'''
x = input ("Enter the input value:")
x = int(x)
if x%2 == 0:
    print ("The given number is an even number")
else :
    print ("The given number is an odd number")
'''
# 9). Python program to check authentication with the given username and password.
'''
a = input("Enter the username: ")
b = input("Enter the password: ")

if a == "username" and b == "password":
    print("Welcome")
else:
    print("Your credentials are wrong")
'''
# 10). Python program to validate user_id in the list of user_ids.
'''
user_ids = [123,456,789,234,567,891]
x = input("Enter the user id: ")
x=int(x)
if x in user_ids :
    print("user id is correct")
else:
    print("user id is invalid")
'''

#11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
'''
x = input("Enter the value: ")
x = int(x)
if x%2 == 0:
    print("The square of the value is:", x**2)
elif x%3 == 0:
    print("The cube of the value is: ",x**3)
else:
    print("The number is not divisible by 2 or 3")
'''

#14). Python program to find the largest number among three numbers.

x = int(input("Enter the first number:"))
y = int(input("Enter the Second number:"))
z = int(input("Enter the Third number:"))

if x>=y and x>=z :
    print ("The greatest number is", x)
elif y>=x and y>=z:
    print ("The greatest number is: ", y)
else:
    print ("The greatest number is", z)

