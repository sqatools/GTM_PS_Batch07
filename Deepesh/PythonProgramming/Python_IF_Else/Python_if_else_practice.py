"""
if <condition>:
    code
else:
    code
"""

a = 20
b = 20

print(a == b)

if a == b:
    print("both variables have same values")
else:
    print("variables values are not same")


# check given number is divisible by 3 or not
num1 = 20

if num1%3 == 0:
    print("Num can divide by 3 :", num1)
else:
    print("Num can not divide by 3:", num1)

# Num can not divide by 3: 20

print("_"*50)
# note :  Else condition is optional, we can use as per requirement
num2 = 700
if num2%7 == 0:
    print("The number can divide by 7:", num2)

######################################
print("_"*50)
# write a python program to check given string has specific character/substring
str1 = "Python Programming"
char = 'p'
if char in str1:
    print("character is available in the string :", char)
else:
    print("character is not available in the string:", char)

print("_"*50)
######################################
"""
# Take input from the user:  input always take user input in string data type.
# we have the data type as per our requirement

var1 = input("Please enter your value1:")
var2 = input("Please enter your value2:")
print("var1 :", var1, type(var1)) # 50 <class 'str'>
print("var2 :", var2, type(var2)) # 100 <class 'str'>
print("Addition :", int(var1)+int(var2))
# Addition : 150

print(list(var1)) # ['5', '6']

"""
################### Logical operators ###############
"""
> : greater than operator
< : less than operator
>= : greater than equal to operator
<= : less than equal to operator
!= : not equal to operator
== : equal to operator

AND condition
cond1 and cond2
True  and False : False
False and True :  False
False and False : False
True and True : True

OR Condition:
cond1 or cond2
True or False :  True
False or True : True
True or True : True
False or False : False
"""
"""
print("_"*50)
num1 = 24
if num1%2 == 0 and num1%3 ==0:
    print("The number is divisible by 2 and 3")
else:
     print("The number is not divisible by 2 and 3")
"""
# The number is divisible by 2 and 3

# same code with or condition
print("_"*50)
num1 = 11
if num1%2 == 0 or num1%3 ==0:
    print("The number is divisible by 2 or 3")
else:
     print("The number is not divisible by 2 or 3")


# The number is not divisible by 2 or 3

print("_"*50)
###############################
"""
If - elif - else

if cond1:
    code
elif cond2:
    code
elif cond3:
     code
elif cond4:
     code
else:
      code
"""


print("_"*50)
# write a python program to check greater number among three values
a = 50
b = 100
c = 100

if a > b and a > c:
    print("A has greater value  :", a)
elif b > a and b >c :
     print("B has greater value  :", b)
elif c >a and c > b:
    print("C has greater value  :", c)
else:
    print("No one has greater value")


"""
# Nested If condition

if cond1:
     code
     if cond2:
        code
        if cond3:
            code
        else:
            code
     else:
        code
else:
    code

"""

print("_"*50)
# write a python program to implement the nested if condition

round1 = 'fail'
round2 = 'fail'
round3 = 'pass'

if round1 == 'pass':
    print("congrats first round is cleared.")
    if round2 == 'pass':
        print("congrats second round is cleared.")
        if round3 == 'pass':
            print("Thi round is cleared")
        else:
            print("Failed in third round")
    else:
        print("sorry second round is not cleared.")
else:
    print("First round is not cleared, try next time")


print("_"*40)
##### Write a python with loop condition ##########

marks= 100
if marks > 100:
    print("Invalid value marks can not be 100")
if marks > 30 and marks <= 40:
    print("Passed with D graf")
if marks > 40 and marks <= 50:
    print("Passed with C graf")
elif marks > 50 and marks <= 70:
    print("passed with B grade ")
elif marks > 70 and marks <= 80:
    print("passed with A grade ")
elif marks > 80 and marks <= 90:
    print("passed with A++ grade ")
elif marks > 90 and marks <= 100:
    print("passed with Excellent grade ")

#q1. write a python program check the person has voting permission or not
# get user age with input keyword.

# Write a python program to print square of value if  divisible by 2 and cube of
# value if divisible by 3.
