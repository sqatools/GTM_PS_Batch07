for i in range(1,10,2):
    print(i)

for j in range(10, 1, -1):
    print(j)
num = 5
for k in range(1,10):
    print(k, "*", num, ":", k*num)

for l in range(1, 50):
    if l%6 == 0:
        print(l)

print("-"*50)

list1 = [1, 3, 6, 78, 12, 65, 87, 23]

for val in list1:
    if val%2 == 0:
        print(val)

str1 = "hello this is satya"

vowels = ["a", "e", "i", "o", "u"]

for char in str1:
    if char not in vowels:
        print(char, end="")
    else:
        pass
print("-"*50)

# write python program to print odd numbers from 1 to 100

for s in range(1, 100):
    if s%2 != 0:
        print(s, end=" ")
print("-"*50)

dist1 = {"a": 100, "b": 200, "c" : 300}

for val in dist1.items():
    print(val)
for k, v in dist1.items():
    print(v)

# num1 = int(input("enter number"))
# prime = True
#
# for i in range(2, num1):
#     if num1%i == 0:
#         prime = False
# if prime:
#     print("this number is prime :", num1)
# else:
#     print("this is not a prime :", num1)

print("-"*50)

num2 = 7
fact = 1

for i in range(num2, 0, -1):
    fact = fact*i
    print(fact)
print(fact)

print("-"*50)
for i in range(1, 10):
    for j in range(i):
        print("*",end="")
    print()

for s in range(5):
    print(s)
print("-"*50)
list21 = [1,2,3,4,5,6,7,8,9]

for val in list21:
    if val%2 == 0:
        print(val)

print("-"*50)

str1 = "hello good morning"

vowels = "aeiou"

for char in str1:
    if char in vowels:
        print(char, end=" ")
    else:
        pass

for r in range(1,100):
    print(r)

print("-"*50)

for i in range(1, 30):
    if i%2 != 0:
        print(i)

dist1 = {"a" : 123, "b" : 456, "c" : 789}

for val in dist1.items():
    print(val)
for k, v in dist1.items():
    print(k)

print("-" * 50)

num3 = 23
prime = True

for i in range(2, num):
    if i%num == 0:
        prime = False
if prime :
    print("this is prime number", num3)
else:
    print("this is not prime", num3)

print("-" * 50)

num4 = 5
fact = 1
for i in range(num4,0,-1):
    fact = fact*i
    print(fact)
print(fact)

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print("-" * 50)

for i in range(1,11):
    for j in range(i):
        print(j, end=" ")
    print()
























