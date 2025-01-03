set1 = {3, 5, 6, 7, 8, 23, 'a', 'b', 7, 8}
print(set1, type(set1))
# {3, 5, 6, 7, 8, 'a', 23, 'b'} <class 'set'>

"""
# set properties :

->  Set is a mutable data type
->  Set only contains unique data, duplicate values are not allowed.
->  All immutable data type can be member in set.
->  Set does not follow indexing.
->  Set store data in random order.
"""

# Set is a mutable data type : Set value can be modify the existing methods e.g. add
set2 = {4, 6, 8, 2}
set2.add(40)

print("set2 :", set2)
# {2, 4, 6, 8, 40}

print("_" * 50)
#  All immutable data type can be member in set.
set3 = {3, 3.5, 'Hello', (5, 6, 78), True, None}
print("set3 :", set3)
# {None, True, 3.5, 3, 'Hello', (5, 6, 78)}

print("_" * 50)
# mutable data type is not allowed as member in set
# set4 = {4, 6, 7, [1, 4, 7]}
# print(set4)
# TypeError: unhashable type: 'list'


##################################
# set5 = {4, 6, 7, {1, 4, 4}}
# print(set5)
# unhashable type: 'set'

# _____________________________________

# set6 = {4, 6, 7, {'a': 1, 'b' : 2, 'c' : 3}}
# print(set6)
# unhashable type: 'dict'

# -------------------------------


print("_" * 50)
# Apply loop on set data
set6 = {4, 6, 8, 2, 66, 11, 44}
for val in set6:
    print(val)

"""
2
66
4
6
8
11
44
"""

#################### Set Methods ########################
print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update',
# 'discard', 'intersection', 'intersection_update',
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
# 'symmetric_difference', 'symmetric_difference_update',
# 'union', 'update'


print("_" * 50)
###################
# add method : This method add one single value at time to the set.
set_7 = {30, 40, 71, 12}
set_7.add(100)
print("set 7:", set_7)
# set 7: {100, 71, 40, 12, 30}


print("_" * 50)
###################
# update method : This method update data from one set top another set.
set_8 = {20, 40, 50, 10, 5}
set_9 = {'a', 'b', 'c', 'd'}

set_9.update(set_8)

print("set_9 :", set_9)
print("set_8 :", set_8)

"""
set_9 : {'b', 5, 'a', 40, 10, 50, 'd', 20, 'c'}
set_8 : {50, 20, 5, 40, 10}
"""

print("_" * 50)
###################
# union method : This method combine 2 sets data and return its output,
# without modifying its original set.

set_10 = {20, 40, 50, 10, 5}
set_11 = {'a', 'b', 'c', 'd'}

result = set_10.union(set_11)
print("combine result result :", result)
# {'d', 5, 40, 10, 'a', 50, 20, 'b', 'c'}


print("_" * 50)
###################
# intersection method : This method return common values from both the sets.
set_12 = {20, 40, 50, 10, 5, 'a', 'b'}
set_13 = {'a', 'b', 'c', 'd', 5, 10}

result = set_12.intersection(set_13)
print('result :', result)  # {'a', 10, 5, 'b'}

# intersection_update : This method update the existing common values between both sets
set_13.intersection_update(result)
print("set 13 :", set_13)
# set 13 : {'a', 10, 5, 'b'}


print("_" * 50)
###################
# difference method : This method return the difference of values among two sets.

set_14 = {20, 40, 50, 10, 5, 'a', 'b'}
set_15 = {'a', 'b', 'c', 'd', 5, 10}

diff_Result1 = set_14.difference(set_15)
print("difference result1 :", diff_Result1)  # {40, 50, 20}

diff_Result2 = set_15.difference(set_14)
print("difference result2 :", diff_Result2)  # {'d', 'c'}

# difference update : update the difference value to existing set.
set_14.difference_update(set_15)  # {50, 20, 40}
print("update result :", set_14)

print("_" * 50)
##################
# symmentric_difference method : This method return the difference values from both sets

set_16 = {20, 40, 50, 10, 5, 'a', 'b', 100}
set_17 = {'a', 'b', 'c', 'd', 5, 10, 200}

sym_diff = set_16.symmetric_difference(set_17)
print("Sym Diff Value :", sym_diff)
# {'c', 100, 40, 200, 'd', 50, 20}


# symmentric_difference udpate method : This method provide the difference of sets value and update to
# existing target set

# set_18 = {'c', 100, 40, 200, 'd', 50, 20}
set_17.symmetric_difference_update(set_16)
# print("set18 :", set_18) # {100, 'c', 40, 200, 50, 20, 'd'}


print("_" * 50)
####################
# pop method : This method remove any random values and return as single value.
set_a = {'c', 100, 40, 200, 'd', 50, 20, 40, 22, 30}
var1 = set_a.pop()
print("removed value :", var1)
print("set_a :", set_a)
# {40, 200, 'c', 'd', 50, 20, 22, 30}


# remove method: Thi method remove any specific value from set.
set_b = {'c', 100, 40, 200, 'd', 50, 20, 40, 22, 30}

# remove available value
set_b.remove(200)
print("removed data :", set_b)
# {100, 40, 50, 'd', 20, 22, 'c', 30}


# remove non exist value
# set_b.remove(500)
"""
# KeyError: 500
"""

print("_" * 50)
###############
# discard() method: This method remove value from set if is available, if the value is not available
# then it does not through any error

set_A = {4, 6, 8, 22, 66, 11}
set_A.discard(22)

print("Set A :", set_A)
# Set A : {66, 4, 6, 8, 11}

# remove value which is not available
set_A.discard(20)
print("Set A :", set_A)

print("_" * 50)
###############
# subset and superset method: subset and superset method check the give set of value is child or parent set values
# or not.
set_p = {'a', 'b', 'c', 'd', 3, 6, 8, 1}
set_q = {'a', 3, 'c'}
set_r = {'b', 'd', 20}

print("set_q is subset of set_p :", set_q.issubset(set_p))
# set_q is subset of set_p : True

print("Set_p is superset of set_q :", set_p.issuperset(set_q))
# Set_p is superset of set_q : True

print("Set_p is superset of set_r :", set_p.issuperset(set_r))
# Set_p is superset of set_r : False


print("_" * 50)
###############
# disjoint() method: This method check the given set is completely different from target set values.

set_x = {'a', 'b', 'c', 'd', 3, 6, 8, 1}
set_y = {'a', 3, 'c', 'e', 'f'}
set_z = {'P', 'Q', 'R'}

result1 = set_x.isdisjoint(set_y)
print("result :", result1)  # False

result2 = set_x.isdisjoint(set_z)
print("result2 :", result2)  # True

print("_" * 50)
###############
# copy method : This method copy content from one set to another.

# Shallow Copy
set_H = {4, 6, 8, 2, 9}
set_J = set_H
set_J.add(100)
print("Set J :", set_J)  # {2, 4, 100, 6, 8, 9}
print("Set H :", set_H)  # {2, 4, 100, 6, 8, 9}

# Deep Copy
set_k = {4, 6, 9, 12, 33, 45}
set_l = set_k.copy()
set_l.add(500)
set_k.add(600)

print("set_k :", set_k)  # {33, 4, 6, 600, 9, 12, 45}
print("set_l :", set_l)  # {33, 4, 500, 6, 9, 12, 45}

# Clear method: This method clear all the data from set
set_k.clear()
print("set_k :", set_k)  # set()
