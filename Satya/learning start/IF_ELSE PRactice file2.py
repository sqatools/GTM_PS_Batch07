# # 34).  Python program to convert the month name to the number of days.
#
# jan = 31
# feb = 28/29
# mar = 31
# apr = 30
# may = 31
# jun = 30
# july = 31
# aug = 31
#
# month = input("enter month")
#
# if month == "jan":
#     print("31")
# elif month == "feb":
#     print("28/29")
from operator import truediv

import bill

print()
# 35). Python program to check whether a triangle is equilateral or not. An equilateral triangle is a triangle in which all three sides are equal.
print("-"*50)

# side_a = int(input("side_a"))
# side_b = int(input("side_b"))
# side_c = int(input("side_c"))
#
# if side_a == side_b == side_c:
#     print("triangle is equilateral")
# else:
#     print("triangle is not equilateral")

print()
# 36). Python program to check whether a triangle is scalene or not. A scalene triangle is a triangle that has three unequal sides.

# print("-"*50)
# side_a = int(input("side_a"))
# side_b = int(input("side_b"))
# side_c = int(input("side_c"))
#
# if side_a != side_b != side_c:
#     print("triangle is scalene")
# else:
#     print("triangle is not scalene")

print()
# 37). Python program to check whether a triangle is isosceles or not. An isosceles triangle is a triangle with (at least) two equal sides.
#
# side_a = int(input("side_a"))
# side_b = int(input("side_b"))
# side_c = int(input("side_c"))
#
# if side_a == side_b != side_c:
#     print("isosceles")
# elif side_a != side_b == side_c:
#     print("isosceles")
# elif side_a == side_c != side_b:
#     print("isoscales")
# elif side_a == side_b == side_c:
#     print("equal triangle")
# elif side_a != side_b != side_c:
#     print("isolate")

# 38). Python program that reads month and returns season for that month.

# jan = "winter"
# feb = "winter"
# mar = "summer "
# apr = "summer"
# aug = "rain"
# sep = "rain"
#
# month = input("enter month")
#
# if month == "jan" or month == "feb":
#     print("winter")
# elif month == "mar" or month == "apr":
#     print("summer")
# else:
#     print("rain")

print()
# 39). Python program to check whether the input number is a float or not if yes then round up the number to 2 decimal places.
print("-"*50)
# num1 = float(input("enter number"))
#
# if type(num1) == float:
#     print(round(num1,2))
# else:
#     print(num1)
#
# num = 25.3614
#
# if type(num) == float:
#     print(round(num,2))
# else:
#     print(num)

# 40). Python program to check whether the input number is divisible by 12 or not.

# num2 = int(input("enter num"))
#
# if num2%12 == 0:
#     print("true")
# else:
#     print("false")
#
# print()

# 41). Python program to check whether the input number is a square of 6 or not.
# num3 = int(input("enter"))
#
# if num3 == 6**2:
#     print("true")
# else:
#     print("false")
print()
# # 42). Python program to check whether the input number is a cube of 3 or not.
#
# num5 = int(input("enter"))
#
# if num5 == 3**3:
#     print("true")
# else:
#     print("f")

# 43). Python program to check whether two numbers are equal or not.

# num6 = 23
# num7 = 23
#
# if num6 == num7:
#     print("equal")
# else:
#     print("not equal")

# 44). Python program to check whether the given input is a complex type or not.
print()

# a = 5+6j
# if type(a) == complex:
#     print(type(a), "true")

# 45). Python program to check whether the given input is Boolean type or not.

a = True

if type(a)== bool:
    print("true")
else:
    print("false")

# 46). Python program to check whether the given input is List or not.
print()
b= [1, 2, 3, 4, 5]

if type(b) == list:
    print("true")
else:
    print("false")

# 47). Python program to check whether the given input is a dictionary or not.

A = {"name" :"virat", "kohli":"cricketer"}

if type(A) == dict:
    print(A)
else:
    print("false")

print()
# 48). Python program to check the eligibility of a person to sit on a roller coaster ride or not. Eligible when age is greater than 12.

# age = int(input("enter age"))
#
# if age >= 15:
#     print("eligible")
# else:
#     print("not")

# 49). Python program to create 10 groups of numbers between 1-100 and find out given input belongs
# to which group using python nested if else statements.

print()

group1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
group2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
group3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# num9 = int(input("enter number"))

# if num9>=1 and num9<=10:
#     print("number id from group1 :", num9)
# elif num9>10 and num9<=20:
#     print("number is from group2 :", num9)
# elif num9>20 and num9<=30:
#     print("num is from group3 :", num9)
# else :
#     print("invalid")

# if num9 in group1:
#     print("no from 1")
# elif num9 in group2:
#     print("no from 2")
# elif num9 in group3:
#     print("no from 3")

print()
print("-"*50)
# 50). Python program to find employees eligible for bonus. A company decided to give a bonus of 10% to employees.
# If the employee has served more than 4 years. Ask the user for years
# served and check whether an employee is eligible for a bonus or not.
# years = int(input("enter no of years"))
#
# if years>= 4:
#     print("eligible")
# else:
#     print("not")

# 51). Take values of the length and breadth of a rectangle from the user and check if it is square or not using the python if else statement.

# length = int(input("length"))
# breadth = int(input("breadth"))
#
# if length == breadth:
#     print("it is square")
# else:
#     print("it is rectangle")

# 52). A shop will give a 10% discount if the bill is more than 1000, and 20% if the bill is more than 2000.
# Using the python program Calculate the discount based on the bill.

#
#

print()
# 53). Python program to print the absolute value of a number defined by the user.
# 54). Python program to check the student’s eligibility to attend the exam based on his/her attendance.
# If attendance is greater than 75% eligible if less than 75% not eligible.

# attend = int(input("enter atta"))
#
# if attend>=75:
#     print("eligible")
# else:
#     print("not eligible")

# 55). Python program to check whether the last digit of a number defined by the user is divisible by 4 or not.
# 56). Python program to display 1/0 if the user gives Hello/Bye as output.

input = input("enter your choice")

if input == 1:
    print("hello")
elif input == 0:
    print("bye")






