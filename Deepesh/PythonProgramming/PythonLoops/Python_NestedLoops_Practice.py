"""
for cond1:
    for cond2
       code
"""
# For each single value of outer loop the entire inner loop is going to execute.

for i in range(1, 5): #i =1
    for val in ['a', 'b', 'c']:
        print(i, val)

    print("_"*50)


print()
"""
* 
* *
* * * 
* * * *
* * * * *
"""

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")

    print()

# for i in range(1, 10):
#      print(i, end=" ")

"""
0 
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4 
"""
for i in range(1, 6):
    for j in range(i):
        print(j, end=" ")

    print()

"""
0 
1 2 
3 4 5 
6 7 8 9 
10 11 12 13 14 
15 16 17 18 19 20 
"""

temp = 0
for i in range(1, 7):
    for j in range(i):
        print(temp, end=" ")
        temp += 1

    print()

"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""

for i in range(1, 7):
    for j in range(1, i):
        print(j, end=" ")

    print()

print("#"*40)
print()

# write a python program to print A pattern
"""
  * * * 
*       *
*       *
* * * * * 
*       *
*       *
*       *
"""
# part1
for i in range(1, 6):
    if i == 1 or i == 5:
        print(" ", end=" ")
    else:
        print("*", end=" ")

# part2
print()
for i in range(1, 3):
    for j in range(1, 6):
        if j == 1 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# part3
for i in range(1, 6):
    print("*", end=" ")

# part4
print()
for i in range(1, 4):
    for j in range(1, 6):
        if j == 1 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



print("#"*40)
print()
# Solution 2
"""
  * * * 
*       *
*       *
* * * * * 
*       *
*       *
*       *
"""

for i in range(1, 8):
    for j in range(1, 6):
        if i == 1:
            if j == 1 or j == 5:
                print(" ", end=" ")
            else:
                print("*", end=" ")

        elif i in [2, 3, 5, 6, 7]:
            if j == 1 or j == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        elif i == 4:
            print("*", end=" ")



    print()
