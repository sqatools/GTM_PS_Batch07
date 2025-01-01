#  Python program to remove negative values from the list.
from itertools import combinations

from Deepesh.PythonProgramming.PythonLoops.Python_Loops_Practice import vowels

list1= [43, 54,65, -32, -1, 56, 23, -65]
result= []
for val in  list1:
    if val > 0 :
        result.append(val)
print(result)
# [43, 54, 65, 56, 23]
#
# Python program to get a list of all elements which are divided by 3 and 7.

list2 = [3, 6, 8, 9, 20, 21, 23, 24, 27, 35, 33, 63]

for val in list2:
    if val%3 ==0 and val%7 == 0:
        print(val)
 # 21
# 63
# Python program to check whether the given list is palindrome or not. (should be equal from both sides).

list3 = ["assa"]

if list3 == list3[::-1]:
    print(list3)
# enter palidrome assa
# ['assa']

print("-"*50)
#Python Program to get a list of words which has vowels in the given string.
list5 = ("hello i am ssss learning python tt cdf gj")
list5_len = list5.split()
voweles = ("a", "e", "i", "o", "u")
result = []
for char in list5_len:
    if any(char in voweles for char in list5_len):
        result.append(char)
print(result)

# Python program to add 2 lists with extend method.
list6 = [1, 2, 3, 4, 5]
list7 = [6, 7, 8, 9]

list6.extend(list7)
print(list6)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list7)
# [6, 7, 8, 9]

# Python program to sort list data, with the sort and sorted method.

list8 = [3, 4, 76, 9, 9]

list8.sort()
print(list8)
#[3, 4, 9, 9, 76]

sorted_list = sorted(list8)
print(sorted_list)
# [3, 4, 9, 9, 76]
#  Python program to remove data from the list from a specific index using the pop method.

list10 = [2, 3, 4, 5, 6, 7]
list10.pop(3)
print(list10)
# [2, 3, 4, 6, 7]


# Python program to get the max, min,
# and sum of the list using in-built functions.
list11 = [5, 8 ,55, 89, 1 ,45]

print(max(list11)) #89

print(min(list11)) # 1
print(sum(list11)) # 203

# Python program to check whether a list contains a sublist.

list12 = [2, 1, 4, [3, 5, 6, 7], 8, 9]
list13 = [8,9]

is_sublist = True

for val in list13:
    if val not in list12:
        is_sublist = False
        break
if is_sublist:
    print("list13 is a sublist of list12")
else :
    print("list13 is a not sublist of list12")

# 28). Python program to generate all sublists
# with 5 or more elements in it from the given list.

from itertools import combinations

list14 = [2, 3, 4, 5, 6, 7, 8, 9, 10]

result = []

for val in range(5, len(list14) + 1):
    for combination in combinations(list14, val):
        result.append(list(combination))
print(result)

print("-"*50)
# 29). Python program to find the second largest number from the list.

list15 = [1, 2, 5, 8, 6, 9, 10]

list15.sort()

print(list15[-2])

# Python program to merge all elements of the list in a single entity using a special character.

list16 = [1, 2, 3, 4]
list17 = [5, 6, 7, 8]
list18 = [9, 10, 11, 12]

list16.extend(list17)
print(list16)

list17.extend(list18)
print(list17)


list20 = ["a", "b", "c"]

merge_string = "$".join(list20)

print(merge_string)
# a$b$c
print()
# Python program to get the difference between two lists.

list21 = [1, 2, 3, 4, 7, 8]
list22 = [5, 6, 7, 8]
result = []
for val in list21:
    if val not in list22:
        result.append(val)
print(result)

# Python program to reverse each element of the list.
print("-"*50)
list23 = ("hello i am learning python")
list23_list = list23.split(" " )

w1 = list23[:5]
w2 = list23[6:7]
w3 = list23[8:10]
w4 = list23[11:19]
w5 = list23[20:26]

W1 = w1[::-1]
W2 = w2[::-1]
W3 = w3[::-1]
W4 = w4[::-1]
W5 = w5[::-1]

result1 = [W1  +  W2  +  W3  +  W4  + W5]
print(result1)





















