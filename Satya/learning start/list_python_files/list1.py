list1 = [12, 45, 56]
for i in list1:
    print(i, end="")
print()
list2 = ["hello", "i", "am", "learning", "python"]

for word in list2:
    print(word, end="")
    # helloiamlearningpython

print()
# Python program to print elements of the list separately.
Input1 =  [("black", "white", "yellow"), (50, 55, 60), (30.0, 50.5, 55.66)]


for i in Input1:
    print(i)
# ('black', 'white', 'yellow')
# (50, 55, 60)
# (30.0, 50.5, 55.66)


#Python program to create a sublist of numbers and their squares from 1 to 10.
result = [[]]
for val in range(1, 10):
    square1 = val**2
    result.append(square1)

print(result)
# [[], 1, 4, 9, 16, 25, 36, 49, 64, 81]

num1 = [(x, x**2) for x in range(1, 11)]
print(num1)
# [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36),
# (7, 49), (8, 64), (9, 81), (10, 100)]

# Python program to insert a given string at the beginning of all items in a list.


list4 = [1, 2, 3, 4]

added_list4 = ["sqa{}".format(item) for item in list4]

print(added_list4)

print("-"*50)

list5 = [1, 2, 3, 4]
list6 = [5, 6, 7, 8]
result = list(zip(list5, list6))
# listed_result = list(result)
print(result)
result5 = []


for list5, list6 in zip(list5, list6):
    result5.append([list5, list6])
#print(result5)

list7 = [1, 2, 3, 4, -5, -3, -8, 7, -1, -3, 8, 9, 10]
var = 0

for val in list7:
    if val > 0:





























