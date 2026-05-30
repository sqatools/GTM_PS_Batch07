#Python Python program to check whether the input number if a multiple of two print “Fizz”
# instead of the number and for the multiples of three print “Buzz”. For numbers that are
# multiples of both two and three print “FizzBuzz”.
# user = int(input("please enter the input number"))
#
# if user%2 == 0 and user%3 == 0:
#     print("fizzbuzz")
# elif user%2 == 0:
#     print("fizz")
# elif user%3 == 0:
#     print("buzz")
#Python program to check whether an alphabet is a vowel.
#
# char = input("enter an alphabit")
# vowels1 = ( "a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
#
# if char in vowels1:
#     print("true")
# else:
#     print("False")
from Deepesh.PythonProgramming.PythonList.Python_List_Concepts import square

#Python program to check whether an alphabet is a consonant.
#
# char = input("enter an alphabit")
# vowels = ( "a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
#
# if char not in vowels:
#     print("true")
# else:
#     print("False")

# #Python program to convert the month name to the number of days.
# month = input("enter month")
#
# if month == "january":
#     print(31)
# elif month == "feb" :
#     print(28,29)
# elif month == "march":
#     print(31)
# elif month =="april":
#     print(30, "days")
# elif month == "may":
#     print(31,"days")
# else:
#     print("invalid month")

# Python program to check whether a triangle is equilateral or not.
# An equilateral triangle is a triangle in which all three sides are equal.

# base = int(input("enter base value"))
# height = int(input("enter the geight"))
# side = int(input("enter the side of triangle"))
# if base == height == side:
#     print(True)
# else:
#     print("its not a equivalent triangle")

#Python program to check whether a triangle is scalene or not.
# A scalene triangle is a triangle that has three unequal sides.
#
# s1 = int(input("enter s1"))
# s2 = int(input("enter s2"))
# s3 = int(input("enter s3"))
#
# if s1 != s2 != s3 :
#     print(True)
# else:
#     print("fasak")

#Python program to check whether a triangle is isosceles or not.
# An isosceles triangle is a triangle with (at least) two equal sides.
#
# s4 = int(input("enter s1"))
# s5 = int(input("enter s2"))
# s6 = int(input("enter s3"))
#
# if s4 == s5 != s6:
#     print(True)
# elif s4 != s5 == s6:
#     print(True)
# elif s4 == s6 != s5:
#     print(True)
# else:
#     print(False)


# Python program that reads month and returns season for that month.
#
# month = input("enter month")
#
# if month == "mar" or month == "apr" or month == "may" or month == "jun":
#     print("summer")
# elif month == "jul" or month == "aug" or month == "sep" or month == "oct":
#     print("rain")
# else:
#     print("winter")

num1 = 25.543

if type(num1) == float:
    print(round(num1, 2))
else:
    print(num1)

#Python program to check whether the input number is divisible by 12 or not.
#
# num2 = int(input("enter number"))
#
# if num2%11 == 0:
#     print(True)
# else:
#     print(False)

#Python program to check whether the input number is a square of 6 or not.
#
# num3 = int(input("enter number"))
# if num3 == 36:
#     print(True)
# else:
#     print(False)

#Python program to check whether the input number is a cube of 3 or not.

# num3 = int(input("enter cube"))
#
# if num3 == 64:
#     print("the entered number is cube of :4")

#Python program to check whether two numbers are equal or not.
#
# n1 = int(input("n1"))
# n2 = int(input("n2"))
#
# if n1 == n2:
#     print("the given numbers are equal")
# else:
#     print("the given number are not equal")
#the given number are not equal
print("-"*50)

#Python program to check whether the given input is a complex type or not.

num5 = 5-6j

if type(num5) == complex:
    print(True)
else:
    print(False)

a = True

if type(a) == bool:
    print(True)
else:
    print(False)

#Python program to check whether the given input is List or not.
a = [2,3,4,5,6]

if type(a) == list:
    print(True)
else:
    print(False)

#Python program to check whether the given input is a dictionary or not.

dist1 = {"name":"satya", "age": 28, "place": "vizag"}
if type(dist1) == dict:
    print(True)
else:
    print(False)

print("-"*50)
#Python program to check the eligibility of a person to sit on a roller coaster ride or not. Eligible when age is greater than 12.
# age = int(input("enter age"))
#
# if age >= 13:
#     print("eligble to sit on a roller coaster")
# else:
#     print("not eligble")

#Python program to create 10 groups of numbers between 1-100 and find out
# given input belongs to which group using python nested if else statements

numb = int(input("enter number"))

if numb in range(1, 11):
    print("the given number belongs to 1st group")
elif numb in range(11, 21):
    print("the given number belongs to 2nd group")
elif numb in range(21, 31):
    print("the given number belongs to 3rd group")
elif numb in range(31, 41):
    print("the given number belongs to 4th group")
elif numb in range(41, 51):
    print("the given number belongs to 5th group")
elif numb in range(51, 61):
    print("the given number belongs to 6th group")
elif numb in range(61, 71):
    print("the given number belongs to 7th group")
elif numb in range(71, 81):
    print("the given number belongs to 8th group")
elif numb in range(81, 91):
    print("the given number belongs to 9th group")
elif numb in range(91, 100):
    print("the given number belongs to 10th group")
else:
    print("not in any group")

#the given number belongs to 3rd group

print("-"*50)

#Python program to find employees eligible for bonus. A company decided to give a bonus of 10% to employees.
# If the employee has served more than 4 years. Ask the user for years served and check whether an employee is
# eligible for a bonus or not.
#
# service = int(input("enter number of years service"))
#
# if service >= 4:
#     print("you are eligble for 10% bonus")
# else:
#     print("you are not eligble for bonus")

#you are eligble for 10% bonus

#Take values of the length and breadth of a rectangle from the user and check if it is square or not
# using the python if else statement.
# lenth = int(input("enter lenght"))
# breadth = int(input("enter the breadth"))
#
# if lenth**2 == lenth*breadth:
#     print("it is a square")
# else:
#     print("it is not a square")

#shop will give a 10% discount if the bill is more than 1000, and 20% if the bill is more than 2000.
# Using the python program Calculate the discount based on the bill.

# bill = int(input("enter total bill amount"))
# discount = 0
# if bill >= 1000 and bill < 2000:
#     discount = 10*(bill/100)
# elif bill >= 2000:
#     discount = 20*(bill/100)
# print("discount amount", discount)

#Python program to print the absolute value of a number defined by the user.

# num = int(input("enter number"))
#
# if num < 0:
#     print(abs(num))
# else:
#     print(num)

#Python program to check the student’s eligibility to attend the exam based on his/her attendance.
# If attendance is greater than 75% eligible if less than 75% not eligible.
#
# attend = int(input("enter attendance"))
#
# if attend >= 75:
#     print("the student is eligble for exams")
# else:
#     print("not eligble")

#Python program to check whether the last digit of a number defined by the user is divisible by 4 or not.

# num = int(input("enter number"))
# last_digit = num%10
#
# if last_digit%4 == 0:
#     print("the last digit is divided by 4")
# else:
#     print('THE LAST DIGIT IS NOT DIVIDED BY 4')

#Python program to display 1/0 if the user gives Hello/Bye as output.
#
# input1 = input("enter your input")
#
# if input1 == "hello":
#     print(1)
# elif input1 == "bye":
#     print(0)

# Python program to accept the car price of a car and display the road tax to be paid
# car_price = int(input("enter price of the car"))
#
# if car_price < 500000:
#     print("tax payable :", 15000)
# elif car_price > 500000 and car_price < 1000000:
#     print("tax payable", 50000)
# elif car_price >1000000:
#     print("tax payable", 80000)


#Using a python program take input from the user between 1 to 7 and print the day
# according to the number. 1 for Sunday 2 for Monday so on.
num = int(input("enter day number"))

if num == 1:
    print("sunday")
elif num == 2:
    print("monday")
elif num ==3:
    print("tuesday")
elif num == 4:
    print("wednsday")
elif num == 5:
    print("thursday")
elif num == 6:
    print("friday")
elif num == 7:
    print("saturday")
else:
    print("invalid")

 #Python program to accept the city name and display its monuments (take Pune and Mumbai as cities).
city = input("enter city name")

if city == "mumbai":
    print("taj", "marine", "lal mahal")
elif city == "pune":
    print("hijiwadi", "toly choke")
elif city == "vizag":
    print("rk beach", "rushikonda")
else:
    print("invalid")


# Python program to check whether the citizen is a senior citizen or not. An age greater than 60 than the given citizen is a senior citizen.

age = int(input("enter the age"))

if age > 60 :
    print("the given citizen is a senior citizen")
else:
    print("not senior citizen")
#Python program to find the lowest number between three numbers.

n1 = 23
n2 = 43
n3 = 34

if n1 > n2  and n1 > n3:
    print("n1 is grater number :", n1)
elif n2 > n1 and n2 > n3:
    print("n2 is grater number;", n2)
elif n3 > n1 and n3 > n2 :
    print("n3 is grater number :", n3)

#Python program to accept the temperature in Fahrenheit and check whether the water is boiling or not.
#Hint: The boiling temperature of water in Fahrenheit is 212 degrees

temp = int(input("enter temperature"))

if temp > 212:
    print("water is boiling")
else :
    print("water is not boiling")


#Python program to accept two numbers and mathematical operations from users and perform mathematical operations according to it.
num1 = int(input("enter num1"))
num2 = int(input("enter num2"))

sum1 = num1 + num2
print(sum1)

#Python program to accept marks from the user allot the stream based on the following criteria.
marks = int(input("enter marks"))

if marks > 85:
    print("science")
elif marks >70 and marks < 85:
    print("commerce")
elif marks >35 and marks < 70:
    print("arts")
elif marks <35 :
    print("fail")
else:
    print("invalid marks")







