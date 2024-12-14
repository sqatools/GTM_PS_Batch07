# num1 = int(input("please enter number"))
# num2 = str(num1)
# if num1 == int(num2[::-1]):
#     print("its a polindrome number")
# else:
#     print("it is not polindrame number")
# print()
# # 17). Python program to check if any given string is palindrome or not.
#
# input = input("please enter input")
#
# if input == str(input[::-1]):
#     print("its a polindrome")
# else:
#     print("its not polindrome")
from http.cookiejar import uppercase_escaped_char

# print()
#
# # 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
# marks = int(input("enter marks"))
#
# if marks>=35:
#     print("student got passed")
# else:
#     print("failed")

# 19). Python program to check whether the given number is positive or not.
# print()
# print("-"*50)
#
# num2 = int(input("enter"))
#
# if num2 >= 1:
#     print("number is positive")
# else:
#     print("negative")

# 20). Python program to check whether the given number is negative or not.
# print("-"*50)
#
# num3 = int(input("enter"))
#
# if num3>= 0:
#     print("false")
# else:
#     print("true")

# 21). Python program to check whether the given number is positive or negative and even or odd.
print()
print("-"*50)
#
# num4 = int(input("go head"))
#
# if num4>= 0:
#     if num4%2 == 0:
#         print("the given number is positive and even")
#     else:
#         print("the given number is positive and odd")
# else:
#     if num4%2 == 0:
#         print("negative numer and even number")
#     else:
#         print("negative number and odd")

# 22). Python program to print the largest number from two numbers.
# num5 = int(input("number"))
# num6 = int(input("num2"))
#
# if num5>num6:
#     print("num5 is grater :", num5)
# else:
#     if num6>num5:
#         print("num6 is grater:", num6)

# 23). Python program to check whether a given character is uppercase or not.
# print()
# str1 = str(input("enter letter"))
#
# if str1.isupper():
#     print("given character is uppercase")
# else:
#     print("given character is not uppercase")
#
# print()
# str2 = str(input("enter letter"))
#
# if str2.islower():
#     print("given character is lowercase")
# else:
#     print("given character is not lowercase")
#
# # 25). Python program to check whether the given number is an integer or not.
# print()
# num8 = input("enter your input")
#
# if num8 is int:
#     print("number is integer")
# else:
#     print("not an integer")

# print("-"*50)
# if type(num8) == int:
#     print("true")
# else:
#     print("false")

# 26).  Python program to check whether the given number is float or not.
#
# print("-"*50)
#
# num9 = 23.
#
# if type(num9) == float:
#     print("true")
# else:
#     print("false")
#
# print("-"*50)
# num10 = 12
#
# if type(num10) == float:
#     print("True")
# else:
#     print("False")
# print()
# if num9 is float:
#     print("true")
# else:
#     print("false")


# 27). Python program to check whether the given input is a string or not.

# str2 = input("write string")
#
# if type(str2) == str:
#     print("true")
# else:
#     print("false")

# 28). Python program to print all the numbers from 10-15 except 13

for i in range(10, 15):
    if i != 13:
        print(i, end=" ")

# 29). Python program to find the electricity bill. According to the following conditions:
print()
# units = int(input("no of units"))
# bill = 0
# if units <= 50:
#     bill = units*.50
#     print("total bill :", bill)
# elif units > 50 and units <= 100:
#     bill = units*.75
#     print("total bill :", bill)
# elif units >100 and units<= 250:
#     bill = units*1.25
#     print("total bill :", bill)
# elif units>250:
#     bill = units*1.50
#     print("total bill :", bill)

# #  30. Python program to check whether a given year is a leap or not.
#
# print()
#
# year = int(input("enter year"))
#
# if year%4 == 0:
#     print("leep year :", year)
# else:
#     print("not a leep year :", year)

print()

# num11 = int(input("enter number"))
#
# if num11%2 == 0 and num11%3 == 0:
#     print("fizzbuzz")
# elif num11%2 == 0:
#     print("fizz")
# elif num11 % 3 == 0:
#     print("buzz")
# print()

vowels = ("A, E, I,O, U")
char = input("enter")
if char in vowels:
    print("its a vowel")
else:
    print("its not a vowel")

print()
vowels = ("A, E, I,O, U, a, e, i, o, u")
char = input("enter")
if char not in vowels:
    print("its a consonant")
else:
    print("its a vowel")













