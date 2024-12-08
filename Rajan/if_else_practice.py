# If else program to assign grades as per total marks.

marks = int(input("Enter the total marks: "))
if marks > 100:
    print("Invalid marks")
elif marks > 90:
    print("Grade: Excellent")
elif marks > 80:
    print("Grade: A++")
elif marks > 70:
    print("Grade: A+")
elif marks > 60:
    print("Grade: B")
elif marks > 50:
    print("Grade: C")
else:
    print("Grade: Fail")
print("_" * 50)
# Python program to check the given number divided by 3 and 5.
number = int(input("Enter a number"))
if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is Not divisible by bth 3 and 5")

print("-" * 50 )

number = int(input("Enter a number: "))
if number % 11 == 0:
    square = number ** 2
    print("The number is divisible by 11.  Its square is:")
else:
    print("The number is Not divisible by 11")
print("_" * 50)
# Program to check if a number is odd or even
number = int(input("Enter a number"))
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

print("-" * 50)
#  Python program to check authentication with the given username and password.
correct_username = "rajan"
correct_password = "password"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print("Authentication is Successful! Welcome")
else:
    print("Authentication Failed! Try Again")