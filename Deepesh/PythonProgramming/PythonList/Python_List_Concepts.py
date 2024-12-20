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
print("_"*50)
print(list_b[-1::-2])  # [44, 22, 50, 20]

# print the list in reverse order
print(list_b[::-1])  # [44, 33, 22, 11, 50, 40, 20]

###################### List Methods #####################
print("_"*50)
print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'


#### Add data to the list ####
print("_"*50)
####
# append() method: This method add one value at a time to the list at end of the list.
list_a = [4, 6, 8, 9]
list_a.append(100)
list_a.append(500)
print("list_a :", list_a) # [4, 6, 8, 9, 100, 500]


print("_"*50)
###########
# insert() method : This method add value at specific index in the list.
list_b = ['a', 'b', 'c', 'd', 'e']
list_b.insert(2, "F")
list_b.insert(-1, "Z")
print("List_b :", list_b)
# ['a', 'b', 'F', 'c', 'd', 'Z', 'e']

list_b.insert(1, {'a': 123, 'b' : 345})
print("List_b :", list_b)
# ['a', {'a': 123, 'b': 345}, 'b', 'F', 'c', 'd', 'Z', 'e']

list_b.insert(2, [3, 4, 5])
print("List_b :", list_b)
# ['a', {'a': 123, 'b': 345}, [3, 4, 5], 'b', 'F', 'c', 'd', 'Z', 'e']


print("_"*50)
###########
# extend() method : -> This method combine one list data to another list,
#                  -> This method modify the existing list values.
#                  -> This method add data at end of target list

list_c = [4, 6, 8, (7, 9, 3)]
list_d = ['p', 'q', 'r', 's']
list_d.extend(list_c)
print("list_d :", list_d) #
# ['p', 'q', 'r', 's', 4, 6, 8, (7, 9, 3)]


print("_"*50)
###########
# list concatenation : through the list concatenation we can combine n number of list data with plus
#                     operator

list_e = [3, 6, 8, 9]
list_f = ['a', 'b', 'c', 'd']
list_g = ['A', 'B', 'C']

result = list_e + list_f + list_g
print("Result :", result)
#  [3, 6, 8, 9, 'a', 'b', 'c', 'd', 'A', 'B', 'C']


print("_"*50)
###########
# multiply list values : we can repeat the list values n number of times with multiplication.

list_h = [3, 5, 7]
result2 = list_h*10
print("Result2 :", result2)
# [3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7]


############### Remove data from list ####################
print("_"*50)
###########
# remove method : This method remove any specific value from list and does not return it.
#                  ->  If any value repeated multiple times, then it will remove first occurrence only
list_j = [3, 5, 7, 9, 44, 22, 7]
list_j.remove(7)
print("list_j :", list_j) # [3, 5, 9, 44, 22, 7]
list_j.remove(44)
print("list_j :", list_j) # [3, 5, 9, 22, 7]


print("_"*50)
###########
# pop method : -> Pop method remove value from specified index position
#              -> Pop method return the remove value, that we can store in any variable
#              -> Default index position is -1

list_k = [33, 55, 77, 12, 33,  23, 34]
# remove from default index -1
v1 = list_k.pop()
print("removed value :", v1) # 34
print("list_k :", list_k)  # [33, 55, 77, 12, 33, 23]

# remove from custom index
v2 = list_k.pop(4)
print("Removed value :", v2) # 33
print("list_k :", list_k) # [33, 55, 77, 12, 23]

print("_"*50)
###########
# clear method () : This method clear all the data from list and remain only empty list
list_p = ['A', 'B', 'C', 'D', 'E']
list_p.clear()
print("List_p :", list_p)
# List_p : []


print("_"*50)
###########
# del function  : del can remove entire variable from memory
                 # del also accept the slicing to remove specific number of values

list_q = [5, 6, 8, 22, 55, 7]

# slicing with del
del list_q[2:5]
print("list_q :", list_q) # [5, 6, 7]

list_r = [5, 6, 8, 22, 7, 22]
del list_r[3::2]
print("list_r :", list_r)  # [5, 6, 8, 7]

# del entire list variable from memory
del list_r
# print("list_r :", list_r)
# NameError: name 'list_r' is not defined. Did you mean: 'list_a'?

###### Data Menupulation in list ####



print("_"*50)
###########
# count method : This method return the number of occurrence of any specific value
list_w = [4, 6, 8, 4, 6, 8, 4]
print("count of 4 :", list_w.count(4))
# count of 4 : 3

print("count of 8 :", list_w.count(8))
# count of 8 : 2



print("_"*50)
###########
# index method : This method return the index position of any specific value
list_x = [44, 55, 77, 12, 34, 12]
print("index of 77 :", list_x.index(77)) #
# index of 77 : 2
print("index of 34 :", list_x.index(34))
# index of 34 : 4


print("_"*50)
###########
# sort method : This method sort the list data in ascending and descending order
#              -> sort method modify the original list and sort the values

list_z = [4, 1, 2, 5, 8, 11, 23, 22]

# sort in ascending order
# list_z.sort()
# print("list_z :", list_z)
# [1, 2, 4, 5, 8, 11, 22, 23]

# sort the list data in descending order
var1 = list_z.sort(reverse=True)
print("list_z :", list_z, var1)
# [23, 22, 11, 8, 5, 4, 2, 1]


print("_"*50)
###########
# sorted function : -> sorted function can sort the list in both ascending and descending order.
#                   -> sorted function does not modify the original list

list_1 = [3, 4, 1, 77, 11, 22, 34]
result1 = list(sorted(list_1))
print("ascending sort result :", result1)
# [1, 3, 4, 11, 22, 34, 77]

result2 = list(sorted(list_1, reverse=True))
print("descending sort result :", result2)
# [77, 34, 22, 11, 4, 3, 1]

print("list 1 :", list_1)
# [3, 4, 1, 77, 11, 22, 34]



print("_"*50)
###########
# reverse() method : This method reverse the list values and modify the original list
#                  -> reverse method does not return anything

list_2 = [3, 1, 17, 2, 7, 13, 15, 44]
list_2.reverse()
print("list_2 :", list_2)
# 44, 15, 13, 7, 2, 17, 1, 3]



print("_"*50)
###########
# reversed() function : This function reverse the list values and return the output
#                       -> This function does not modify the original list

list_3 = [4, 6, 11, 66, 22, 77, 99]
result = list(reversed(list_3))
print("reverse result :", result)
print("list_3 :", list_3)
