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

'''
'''
# 15). Python program to check any person eligible to vote or not

x = int(input("Enter your age:"))

if x>= 18 :
    print("You are eligible to vote")
else:
    print("You are not eligible for vote")
'''
# 16). Python program to check whether any given input is a palindrome.
'''
x = input("Enter the input:")

y = x[::-1]

if x == y :
    print ("The given input is a palindrome")
else :
    print("The given input is not a palindrome")
'''
# 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
'''
x = int(input("Enter the mark:"))

if x>= 35:
    print("PASS")
else :
    print("FAIL")
'''
# 19). Python program to check whether the given number is positive or negative.
'''
x = int(input("Enter the number:"))

if x >= 0:
    print("The number is positive")
else :
    print("The number is negative")
'''
# 21). Python program to check whether the given number is positive or negative and even or odd.
'''
x = int(input("Enter the number:"))

if x>=0:
    if x%2 == 0:
        print("The given number is positive and even")
    else:
        print("The given number is positive and odd")
else :
    if x%2 == 0:
        print("The given number is negative and even")
    else:
        print("The given number is negative and odd")
'''
# 22). Python program to print the largest number from two numbers.
'''
x = int(input("Enter the first number:"))
y = int(input("Enter the Second number:"))

if x>=y:
    print("The largest number is: ", x)
else:
    print("The largest number is: ", y)
'''
# 32). Python program to check whether an alphabet is a vowel.
'''
vowel = ['A','E','I','O','U','a','e','i','o','u']
x=input("Enter the character: ")

if x in vowel :
    print("The given character is a vowel")
else :
    print("The given character is not a vowel")
'''

# 34).  Python program to convert the month name to the number of days.
'''
x=input("Enter the Month: ")

if x == ("january" or "march" or "may" or "july" or "august" or "october" or "december") :
    print ("Number of days is 31")
elif x == ("april" or "june" or "september" or "november"):
    print("Number of days is 30")
elif x == ("february"):
    print("Number of days is 28 or 29")
else:
    print("Invalid Month")
'''

# 52). A shop will give a 10% discount if the bill is more than 1000, and 20% if the bill is more than 2000. Using the python program Calculate the discount based on the bill.
'''
x = int(input("Enter the total bill amount: "))

if 2000 >= x > 1000 :
    print ("The discount is 10%")
elif x> 2000:
    print ("The discount is 20%")
else:
    print("No discount")
'''
'''
for x in range(1, 101):
    print(x)

for y in range(1,21):
    if y%2!=0 :
        print(y)
'''