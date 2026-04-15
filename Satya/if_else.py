a = 20
b = 10

if a==b:
    print("both values are same")
else:
    print("both vare are not same")

#  both vare are not same

num1 = 21

if num1%3 == 0:
    print("number is divisible by 3")
else:
    print("number is not divisible by 3")
# number is divisible by 3

#var1 = input("please enter value1")
#var2 = input("enter value2")

#print(var1+var2)
#print(int(var1)+int(var2))

print("-"*50)

num2 = 18

if num2%2 == 0 and num2%3 == 0:
    print("num1 is divided by both 2 & 3")
else:
    print("num2 is not divided by 2 & 3")

# write a program to check which number is greater

a = 55
b = 60
c = 60

if a > b and a > c:
    print("a has grater value")
elif b>a and b>c:
    print("b has a grater value")
elif c>a and c>b:
    print("c has grater value")
else:
    print("no one has grater value")

print("-"*50)

round1 = "pass"
round2 = "pass"
round3 = "fail"

if round1 == "pass":
    print("congrats 1st round cleared")
    if round2 == "pass":
        print("2nd round is cleared")
        if round3 == "pass":
            print("congrats you are cleared all rounds")
        else:
            print("sorry you are not cleared 3rd round")
    else:
        print("sorry 2nd round is not cleared")

else:
    print('sorry you are not cleared 1st round')

print("-"*50)

marks = 30

if marks > 40 and marks < 50:
    print("passed with grade d", marks)
elif marks >= 50 and marks < 60:
    print("passed with grade c", marks)
elif marks >= 60 and marks < 70:
    print("passed with grade b", marks)
elif marks >= 70 and marks <80:
    print("passed with grade a")
elif marks >= 80 and marks < 90:
    print("passed with grade a+")
elif marks >= 90:
    print("passed with a++")
else:
    print('failed')

print("-"*50)

user_age = 18

if user_age >= 18:
    print("user is eligble for voting", user_age)
else:
    print("user is not eligble for voting", user_age)

print("-"*50)

# Python program to check given number is divided by 3 or not

num1 = 23

if num1%3 == 0:
    print("num1 is divided by 3", num1)
else:
    print("num1 is not divided by 3", num1)

# If else program to get all the numbers divided by 3 from 1 to 30

for i in range(1, 30):
    if i %3 == 0:
        #print(i, end=" ")
        print(i)

print("-"*50)

# 4. Python program to check the given number divided by 3 and 5.

num3 = 15

if num3%3 == 0 and num3%5 == 0:
    print("number is divided by 3&5 :", num3)
else:
    print("number is not divided by 3&5", num3)

#Python program to print the square of the number if it is divided by 11.

num4 = 23

if num4 % 11 == 0:
    print(num4**2)
else:
    print("number is not divided by 11", num4)

# Python program to check given number is a prime number or not.
# Python program to check given number is odd or even

num6 = 23

if num6 %2 == 0:
    print("number is even", num6)
else:
    print("number is odd")

# Python program to check a given number is part of the Fibonacci series from 1 to 10.
# fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# value3 = int(input("enter number"))
#
# if value3 in fib:
#     print("it is a part of fib")
# else:
#     print("it is not part of fib")

# Python program to check authentication with the given username and password.
print("-"*50)
# Python program to check authentication with the given username and password.
#user_name = input("enter username")
#password = input("enter password")

#if user_name == password:
   # print("it is valid")
#else:
   # print("it is not valid")

user_name = "satya"
password = "santhi"

user_name_input = "satya"
username_password = "santhi"

if user_name_input == user_name and username_password == password:
    print("its valid")
else:
    print("its not valid")

print("-"*50)
# Python program to validate user_id in the list of user_ids.
list1 = ["satya@309", "santhi@143", "rama@civil"]

user_id = "satya@309"

if user_id in list1:
    print("it is valid")
else:
    print("it is not valid")

print("-"*50)

# Python program to print a square or cube if the given number is divided by 2 or 3 respectively
# number1 = int(input("enter number"))
#
# if number1%2 == 0 and number1%3 == 0:
#     print(number1**2)
# else:
#     print("it is not divided by 2 & 3")

print("-"*50)

#Python program to describe the interview process
round4 = "pass"
round5 = "pass"
round6 = "pass"

if round4 == "pass":
    print("congrats you are cleared round4")
    if round5 == "pass":
        print("congrats you are passed 5th round")
        if round6 == "pass":
            print("congrats you got job")
        else:
            print("sorry you are not cleared the final round")
    else:
        print("sorry you are not cleared 5th round")
else:
    print("sorry you are not cleared round4")

print("-"*50)
# Python program to determine whether a given number is available in the list of numbers or not.

# list5 = [1,2,3,4,5,6,7,8,9]
#
# numb = int(input("enter numb"))
#
# if numb in list5:
#     print("number is valid")
# else:
#     print('number is not availble in the list')

# Python program to find the largest number among three numbers.
number1 = 60
number2 = 30
number3 = 50

if number1 > number2 and number1 >number3:
    print("number1 is grater")
if number2 > number1 and number2 > number3:
    print("number2 is grater")
if number3 > number1 and number3 > number1:
    print("number3 is grater")
else:
    print("no number is grater")

num5 = 121
num6 = str(num5)

if num5 == int(num6[::-1]):
    print("its a palindrome number")
else:
    print("its a not a palindrome number")

print("-"*50)
# Python program to check if any given string is palindrome or not
str1 = "jaj"

if str1 == str1[::-1]:
    print('its a palindrome')
else:
    print("its not a palindrome")

print("-"*50)

# Python program to check whether the given number is positive or not.
numb5 = 20

if num5 > 0:
    print("number is positive")
else:
    print("number is negative")

#Python program to check whether the given number is positive or negative and even or odd.
numb6 = 26

if numb6 > 0 :
    if numb6%2 == 0:
         print("number is positive and even")
    else:
        print("number is positive and odd")
else:
    if numb6 % 2 == 0:
        print("number is positive and even")
    else:
        print("number is positive and odd")

print("-"*50)
# Python program to check whether a given character is uppercase or not

# char2 = input("enter char")
#
# if char2.isupper():
#     print("true")
# else:
#     print("false")

# Python program to check whether the given character is lowercase or not.

# char3 = input("enter char")
#
# if char3.islower():
#     print("true")
# else:
#     print("false")
# Python program to check whether the given number is an integer or not.

int1 = 42

if int1.is_integer():
    print('true')
else:
    print("false")

if type(int1) == int:
    print("true")

#Python program to check whether the given number is float or not

float1 = 23.5

if type(float1) == float:
    print("true")
else:
    print("false")

# Python program to check whether the given input is a string or not
str4 = 'satya lovers santhi'

if type(str4) == str:
    print("true")
else:
    print("false")
# Python program to print all the numbers from 10-15 except 13

for i in range(10, 15):
    if i != 13:
        print(i)

# Python program to find the electricity bill. According to the following conditions:

# units1 = int(input("enter units"))
#
# if units1 < 50:
#     print(units1*0.5)
# if units1 >= 50 and units1 <100 :
#     print(units1*0.75)
# if units1 >= 100 and units1 < 250:
#     print(units1*1.25)
# if units1 >250:
#     print(units1*2)
#
print("-"*50)


# Python program to check whether the given number is an integer or not

# num7 = input("enter number")
#
# if num7 == int:
#     print("true")
# else:
#     print("false")

# Python program to check whether a given year is a leap or not.

year = 2000

if year%4 == 0:
    print("it is leep year")
else:
    print("it is not a leep year")

# 31). Python Python program to check whether the input number if a multiple of two print “Fizz” instead of the number and for the multiples of three print “Buzz”. For numbers that are multiples of both two and three print “FizzBuzz”.

num8 = 6

if num8%2 == 0:
    print("fizz")
elif num8%3 == 0:
    print("buzz")
elif num8%2 == 0 and num8%3 == 0:
    print("fizzbuzz")

# Python program to check whether an alphabet is a vowel.
# list3 = ["a", "e", "i", "o", "u"]
#
# char2 = str(input("enter charcter"))
#
# if char2 not in list3:
#     print("true")
# else:
#     print('false')

# Python program to convert the month name to the number of days

month = "feb"

if month == "january":
    print("31")
elif month == "feb":
    print("28/29")

print("-"*50)

# 35). Python program to check whether a triangle is equilateral or not. An equilateral triangle is a triangle in which all three sides are equal

side1 = 10
side2 = 10
side3 = 10

if side1 == side2 == side3:
    print("it is equalateral triangle")
else:
    print("it is not equaliteral triangle")

# 38). Python program that reads month and returns season for that month.

summer = ["mar", "apr", "may", "june"]
rain = ["jul", "aug", "sep", "oct"]
winter = ["nov", "dec", "jan", "feb"]

month1 =  "feb"

if month1 in summer:
    print("it is summer")
elif month1 in rain:
    print("it is rain season")
elif month1 in winter:
    print("it is winter")

# 39). Python program to check whether the input number is a float or not if yes then round up the number to 2 decimal places.

float1 = 24.3456

if type(float1) == float:
    print(round(float1,2))
else:
    print(float1)