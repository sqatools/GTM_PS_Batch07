a = 10
print(a)
d = str(a)
print("type of d",type(d))
print("type of a",type(a))
b=30
print(b)
print(type(b))

s = 'satya'
print(type(s))

x,y,z = 20,40,50

print(x)
print(y)
print(z)

print("value of x+y", x+y)

print("division of z//x", z//x)

print(a**3)
#Python program to generate random numbers
print("-"*50)
import random

for i in range(5):
    print(random.random())

# Python program to generate a random string with a specific length

import string
import random
print("-"*50)

# 50num = int(input("enter number"))
#
# print(f"binary form of {num}",",".format(num))

print("-"*50)
# dict conversations
dict1 = {"a" : 123, 'b' : 345, "c": "satya"}
str1 = str(dict1)
print(str1[17]) # 4

list1 = list(dict1)
print(list1) #['a', 'b', 'c']

tup1 = tuple(dict1)
print(tup1) # ('a', 'b', 'c')

set1 = set(dict1)
print(set1) # {'c', 'a', 'b'}

dict2 = {}
dict3 = {"name" : "satya", "age" : 28}

b1 = bool(dict2)
b2 = bool(dict3)
print(b1) #False
print(b2, type(b2)) # True <class 'bool'>


print("-"*50)
# set conversations

set1 = {4,3,5,6,7}

str1 = str(set1)
print(str1, type(str1)) # {3, 4, 5, 6, 7} <class 'str'>

list1 = list(set1)
print(list1, type(list1)) # [3, 4, 5, 6, 7] <class 'list'>

tup3 = tuple(set1)
print(tup3, type(tup3)) # (3, 4, 5, 6, 7) <class 'tuple'>

set_a = set()
b1 = bool(set_a)
print(b1) # False

set_b = {345,456,766}
b2 = bool(set_b)
print(b2, type(b2)) # True <class 'bool'>


########## boolean conversation

var1 = True
n1 = int(var1)
print(n1)  #1

var2 = False
n2 = int(var2)
print(n2)  #0


var3 = True
n4 = float(var3)
print(n4)  ## 1.0


var4 = True
n5 = str(n4)
print(n5, type(n5))  ##1.0 <class 'str'>

# var5 = True
# n6 = list(var5)
# print(n6, type(n6)) #TypeError: 'bool' object is not iterable
