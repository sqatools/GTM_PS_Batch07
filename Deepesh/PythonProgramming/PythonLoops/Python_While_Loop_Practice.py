"""
while condition:
    code
"""

num1 = 1
while num1 <= 20:
    print(num1, end=" ")
    num1 += 1

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# infinite loop : This loop will execute until stopped forcefully
"""
n1 = 5
while True:
    print(n1)
    n1 += 5
"""

print()
# break and continue keyword
# continue statement
print("_"*50)
v1 = 1
while v1 <= 10:
    if v1 == 4 or v1 == 5:
        v1 += 1
        continue
    print(v1)
    v1 += 1


# continue statement
print("_"*50)
v2 = 1
while v2 <= 10:
    if v2 == 4:
        v1 += 1
        break
    print(v2)
    v2 += 1



# break the infinite loop in specific condition

n1 = 5
while True:
    print(n1)
    n1 += 5
    if n1 > 100000:
        break
