"""
# -> Properties:
-> List is mutable data type
-> List follows positive and negative indexing
-> List can contain any type of data, int, float, string, list, dictionary, set, boolean
-> we define list with square bracket
"""

list1 = [2, 3.4, 'Hello', [3, 4, 5], (3, 7, 1), {'a' : 23, 'b' : 456}, True]
print(list1, type(list1))

# [2, 3.4, 'Hello', [3, 4, 5], (3, 7, 1), {'a': 23, 'b': 456}, True] <class 'list'>

# List follows indexing
print(list1[-3])  # (3, 7, 1)
print(list1[2])  # Hello
print(list1[3])  # [3, 4, 5]
print(list1[3][1])  # 4
print(list1[-2]['b'])  # 456


print("_"*50)
### Apply Loop on List data ####

list_a = [3, 6, 9, 12, 45]

# without index
for val in list_a:
    print(val)
"""
3
6
9
12
45
"""

print("_"*50)
# with indexing
list_len = len(list_a)
for i in range(list_len):
    print(i, list_a[i])

"""
0 3
1 6
2 9
3 12
4 45
"""

print("_"*50)
############### List Slicing #############
list_b = [20, 40, 50, 11, 22, 33, 44]

print(list_b[1:4])  # [40, 50, 11]
print(list_b[-4:-1])  # [11, 22, 33]
print(list_b[2:7]) # [50, 11, 22, 33, 44]
print(list_b[2:]) # [50, 11, 22, 33, 44]
print(list_b[-1:-6:-1])  # [44, 33, 22, 11, 50]
print(list_b[:-6:-1]) # [44, 33, 22, 11, 50]
