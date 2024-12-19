# 1). Write a  Python loops program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).
for i in range(1500, 2700):
    if i%7 == 0 and i%5 == 0:
        print(i)

print()
rows = 5

for i in range(1, rows+1):
    print("* " *i)

for i in range(rows -1, 0, -1):
    print("* "*i)


print()
rows = 10
for i in range(1, rows+1):
    print("#$ "*i)
for i in range(rows -1, 0, -2):
    print("#$ "*i)

# 3). Python Loops program that will add the
# word from the user to the empty string using python.
print()

# word = input("enter word")
# result = " "
#
# for i in range(len(word)):
#     result += word[i]
# print("enter word :", result)

# 4). Python Loops program to count the number of even and
# odd numbers from a series of numbers using python.

print()

satya = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = 0
odd = 0
for i in satya:
    if i%2 == 0:
        even += 1

    else:
        odd += 1

print("even number :", even)
print("odd number :", odd)


print()
rows = 20
for i in range(3, rows+1):
    print("*"*i)
for i in range(rows -1, 0, -1):
    print("*"*i)