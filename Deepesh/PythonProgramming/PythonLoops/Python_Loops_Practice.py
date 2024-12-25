"""
1. For Loop
2. Nested For Loop
3. While Loop
"""
# range(initial value, end value, difference)
# In the output of range initial value will be included and last value will exclude.

for i in range(1, 10, 1):
    print(i)


print("_"*50)
for i in range(1, 10, 2):
    print(i)


print("_"*50)
# default initial value is zero and default difference is 1
for j in range(5):
    print(j)

# get reverse value with negative difference
print("_"*50)
for k in range(10, 0, -1):
    print(k)


print("_"*50)
# write a python program to print the table of any given number
num = 6
for i in range(1, 11):
    print(i, "*", num, ":", i*num)


# apply if condition in the loop
# Get all the number which are divisible by 3 and 5 between 1 to 50
print("_"*50)

for i in range(1, 50):
    if i%3 == 0 and i%5 == 0:
        print(i)
    else:
        pass


# get value in negative
print("_"*50)
for i in range(-10, 0, 1):
    print(i)



print("_"*50)
# Apply loop in list
list1 = [4, 5, 7, 22, 55, 77]
for val in list1:
    #print(val)
    if val%2 == 0:
        print(val)

"""
4
22
"""


# write a python to get string values
str1 = "Hello Good Morning"
vowels ='aeiou'
for char in str1:
    if char not in vowels:
        print(char, end=" ")
    else:
        pass

print()
# write a python to print value from 1 to 100
# write a python print all odd values from 1 t0 20

# apply loop on dictionary values
print("_"*50)
dict1 = {'a': 123, 'b' : 456, 'c' : 567}
for val in dict1.items():
    print(val)
"""
('a', 123)
('b', 456)
('c', 567)
"""

for k, v in dict1.items():
    print(v)

"""
123
456
567
"""


######################################
# write a python program to check given number is prime or not
print("_"*50)
num = 13
result = True

for i in range(2, num): # i = 2
    if num%i == 0: # 12%2 == 0
        result= False

if result:
    print("This is prime number :", num)
else:
    print("This is not a prime number", num)



print("_"*50)
# write a python program to get factorial of any nnumber
# fact 5 = 5*4*3*2*1
num1 = 6
fact = 1
for i in range(num1, 0, -1):
    fact = fact*i
    print(fact)

print("Factorials of num1 :", fact)
# Factorials of num1 : 720

value1 = 345
str1 = str(value1)[::-1]
print(str1)

###################################################################
