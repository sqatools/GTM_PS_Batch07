########## Integer ###########

# int -> float #

num1= 40
num2 = float(num1)
print(num2, type(num2))
# 40.0 <class 'float'>

print("_"*50)
### int -> string ###

num_a = 3456
str1 = str(num_a)
print(str1, type(str1), str1[2])
# 3456 <class 'str'> 5

print("_"*50)
### int -> list ###  conversion is not possible
"""
a = 567
list1 = list(a)
print(list1)
# TypeError: 'int' object is not iterable
"""

### int -> tuple ### conversion is not possible
## int -> dict ### conversion is not possible
## int -> set ### conversion is not possible

### int -> boolean ###
p = 0
b1 = bool(p)
print(b1, type(b1))
# False <class 'bool'>

q = 101
b2 = bool(q)
print(b2, type(b2))
# False <class 'bool'>

r = -102
b3 = bool(r)
print(b3, type(b3))
# True <class 'bool'>

####################################### Float ####################
print("_"*50)
# float  -> int ##
A = 50.45
n1 = int(A)
print(n1, type(n1))
# 50 <class 'int'>


print("_"*50)
# float  -> string ##
B = 45.55
str1 = str(B)
print(str1, type(str1), str1[-1])
# 45.55 <class 'str'> 5


print("_"*50)
# float  -> list ## conversion is not possible
# float ->  tuple ## conversion is not possible
# float -> dict ## conversion is not possible
# float -> set ### conversion is not possible

# float -> set ##
f1 = 0.0
b1 = bool(f1)
print(b1, type(b1))
# False <class 'bool'>

f2 = 56.78
b2 = bool(f2)
print(b2,  type(b2))
# True <class 'bool'>


########################## String ########################
print("_"*50)

## string ->  int ###
""""
str_a = "Hello"
num_a = int(str_a)
# ValueError: invalid literal for int() with base 10: 'Hello'
"""

# if string only contains number with any special character or space
# then conversion is possible

str_b = "454"
print(str_b*2)  # 454454
num_b = int(str_b)
print(num_b, type(num_b), num_b*10)
# 454 <class 'int'> 4540


print("_"*50)
### string -> float ###

# if string only contains num/pointer value then conversion is possible
str_c = "56.789"
num_c = float(str_c)
print(num_c, type(num_c), num_c*100, num_c*2)
# 56.789 <class 'float'> 5678.900000000001, 113.578


print("_"*50)
### string -> list ###
str_d = "Python"
list_d = list(str_d)
print(list_d, type(list_d))
# ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'>


print("_"*50)
### string -> tuple ###
str_e = "Programming"
tup_e = tuple(str_e)
print(tup_e, type(tup_e))
# ('P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g') <class 'tuple'>


print("_"*50)
### string -> dictionary ###

"""
str_f = "Good"
dict_f = dict(str_f)
print(dict_f)
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
"""

import json

details = '{"Name" : "John", "Email" : "john@gmail.com", "Phone": 343434}'
print(details, type(details))
# {"Name" : "John", "Email" : "john@gmail.com", "Phone": 343434} <class 'str'>

data = json.loads(details)
print(data, type(data))
# {'Name': 'John', 'Email': 'john@gmail.com', 'Phone': 343434} <class 'dict'>

print(data['Name']) # John
data['city'] = 'Mumbai'
print(data)
# {'Name': 'John', 'Email': 'john@gmail.com', 'Phone': 343434, 'city': 'Mumbai'}




print("_"*50)
### string -> set ###
str_g = "Hello"
set_g = set(str_g)
print(set_g)
# {'l', 'o', 'e', 'H'}

print("_"*50)
### string -> set ###

str_j = ""
b1 = bool(str_j)
print(b1, type(b1))
# False <class 'bool'>

str_k = "Python"
b2 = bool(str_k)
print(b2, type(b2))
# True <class 'bool'>



###################### List #################
# list -> int ### conversion is not possible
# list -> float ###  conversion is not possible\

print("_"*50)
# list ->  string ###
list_a = [3, 5, 6, 7]
str_a = str(list_a)
print(str_a, type(str_a))
print(str_a[0], str_a[1], str_a[2])
# [ 3 ,


print("_"*50)
# list ->  string ###
list_r = [5, 8, 1, 6]
tup_r = tuple(list_r)
print(tup_r, type(tup_r))
# (5, 8, 1, 6) <class 'tuple'>

print("_"*50)
# list ->  dictionary ###
"""
list_y = [4, 6, 8, 12]
dict_y = dict(list_y)
print(dict_y)
# cannot convert dictionary update sequence element #0 to a sequence
"""

list1 = ['a', 'b', 'c', 'd']
list2 = [20, 30, 40, 50]

result = dict(zip(list1, list2))
print(result)
print(result, type(result))
# {'a': 20, 'b': 30, 'c': 40, 'd': 50} <class 'dict'>


print("_"*50)
### list ->  set ###
list_x = [4, 6, 8, 4, 5, 2, 4, 5]
set_x = set(list_x)
print(set_x, type(set_x))
# {2, 4, 5, 6, 8} <class 'set'>


print("_"*50)
### list ->  Boolean ###
list_z = [4, 6, 8, 12, 45, 56]
print(list_z, type(list_z))
b1 = bool(list_z)
print(b1, type(b1))
# True <class 'bool'>

list_m = []
b2 = bool(list_m)
print(b2, type(b2))
# False <class 'bool'>



############################## Tuple ######################
# tuple -> int ## conversion is not possible
# tuple -> float ## conversion is not possible

print("_"*50)
# tuple -> string ##
tup_a = (4, 6, 7, 8)
str_a = str(tup_a)
print(str_a, type(str_a), str_a[0], str_a[1])
# (4, 6, 7, 8) <class 'str'> ( 4


print("_"*50)
## tuple -> list ##
tup_b = (4, 7, 9, 23)
list_b = list(tup_b)
print(list_b, type(list_b))
# [4, 7, 9, 23] <class 'list'>


print("_"*50)
## tuple -> dictionary ##
# direct conversion is not possible

t1 = ('X', 'Y', 'Z')
t2 = (122, 456, 789)

result = dict(zip(t1, t2))
print(result, type(result))
# {'X': 122, 'Y': 456, 'Z': 789} <class 'dict'>


print("_"*50)
### tuple -> set ####
tup_d = (4, 5, 6, 4, 5, 7, 2)
set_d  = set(tup_d)
print(set_d, type(set_d))
# {2, 4, 5, 6, 7} <class 'set'>


print("_"*50)
### tuple -> bool ####

tup_e = ()
print(tup_e, type(tup_e))
b1 = bool(tup_e)
print(b1, type(b1))
# False <class 'bool'>

tup_f = (5, 7, 89)
b2 = bool(tup_f)
print(b2, type(b2))
# True <class 'bool'>
