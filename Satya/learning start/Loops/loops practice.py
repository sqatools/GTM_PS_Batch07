#1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
import string

for i in range(1500, 2700):
    if i % 7 ==0 and i%5 == 0:
        print(i)

print("-"*50)
####
# 2). Python Loops program to construct the following pattern, using a nested for loops.
# Output :
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *

# ####

for i in range(6):
    print(i*"*")
for j in range(4,-1,-1):
    print(j*"*")

print("-"*50)
# ). Python Loops program that will add the word from the user to the empty string using python.

word = ("hello")
str1 = ""
for i in range(len(word)):
    str1 += word[i]
print(str1) # hello

#). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
print("-"*50)

for i in range(1,10):
    if i%2 == 0:
        print(i,"this is even numers")
    else:
        print(i, "this are odd numbers")

numbers = (1,2,3,4,5,6,7,8,9)
even = 0
odd = 0

for val in numbers:
    if val%2 == 0:
        even += 1
    else:
        odd += 1
print(even,"numbers of even numbers")
print(odd, "number of odd numbers")

print("-"*50)

#5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.

for i in range(1, 7):
    if i != 3 and i != 6:
        print(i)

# 6). Write a program to get the Fibonacci series between 0 to 20 using python.
print("-"*50)
# 7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
# For numbers that are multiples of both three and five print “FizzBuzz”.

for i in range(1, 30):
    if i%3 == 0:
        print("fizz")
    if i%5 == 0:
        print("buzz")
    if i%3 == 0 and i%5 == 0:
        print("fizzbuzz")

#8). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
print("-"*50)
word = "SATYA"
result = " "
for char in word:
    if char.isupper():
        print(char.lower(), end="")
    else:
        print(char, end=" ")

#9). Python loops program that accepts a string and calculates the number of digits and letters using python.
print("-"*50)
word1 = "satya143"
char = 0
numb = 0

for i in word1:
    if i.isalpha():
        char += 1
    else:
        numb += 1
print("number of char",char)
print("number of letters", numb)


###
# 10). Python for loop program to print the alphabet pattern ‘O’ using python.
# Output:
#   ***
# *       *
# *       *
# *       *
# *       *
# *       *
#   ***
# ###
print("-"*50)
for i in range(1,6):
    if i == 1 or i == 5:
        print(" ", end="")
    else:
        print("*", end="")
print()
for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or j == 5:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,6):
    if i == 1 or i == 5:
        print(" ", end="")
    else:
        print("*", end="")

print("-"*50)
#11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.
n = 8
count = 1

while count <= n:
    print(count,end="")
    count += 1

print("-"*50)
n = 5
count = n
while count != 0:
    print(count, end="")
    count -= 1
print("-"*50)

num = 20
count = n

while count != 0:
    print(count, end=" ")
    count -= 1


#13). Python Loops program to print all alphabets from a to z using for loop
        # Take chr method help to print characters with ASCII values
        # chr(65) = ‘A’
        # A-Z ASCII Range  65-90
        # a-z ASCII Range  97-122

for letter in string.ascii_lowercase:
    print(letter, end=" ")
for letter in string.ascii_uppercase:
    print(letter, end=" ")
print("-"*50)

# 14). Python Loops program to print all even numbers between 1 to 100 in python.

for i in range(1, 100):
    if i %2 != 0:
        print(i, end=" ")

for i in range(1, 100):
    if i %2 == 0:
        print(i, end=" ")

# 16). Python Loops program to find the sum of all natural numbers between 1 to n using python.
print("-"*50)

n = 10
count = 0


    