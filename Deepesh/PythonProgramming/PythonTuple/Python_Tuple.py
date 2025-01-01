tup1 = (3, 5, 7, 8, 12, 5, 7)
print(tup1, type(tup1))
# (3, 5, 7, 8, 12, 5, 7) <class 'tuple'>

"""
-> Tuple is the immutable data type. once it is defined than we can
   not modify it.
->  Tuple follows positive and negative as like string and list
->  Tuple can contains all the type of data, int, float, string, dictionary, set, boolean
->  Tuple is faster than list in terms of performance.
"""

tup2 = (
    3, 43.5, 'Hello', [3, 5, 7],
    (7, 8, 9), {'a' : 123, 'b' : 345, 'c' : 3343},
    {4, 6, 7}, True, False
)

print(tup2[2]) # Hello
print(tup2[-4]['b']) # 345
print(tup2[3][2]) # 7
print(tup2[6:]) # ({4, 6, 7}, True, False)
print(tup2[2::2])  # ('Hello', (7, 8, 9), {4, 6, 7}, False)
print(tup2[-1::-2])  # (False, {4, 6, 7}, (7, 8, 9), 'Hello', 3)
print(tup2[::-1]) # (False, True, {4, 6, 7}, {'a': 123, 'b': 345, 'c': 3343}, (7, 8, 9), [3, 5, 7], 'Hello', 43.5, 3)

print("_"*50)
############## Apply loop on tuple ###########
tup3= (3, 5, 8, 2, 9)

# without index
for val in tup3:
    print(val)

print("_"*50)
# with index
for i in range(len(tup3)):
    print(i, tup3[i])

print("_"*50)
# Methods in the tuple
print(dir(tuple))

# 'count', 'index'

# count method: this get occurrence of any value.
tup_a = (3, 6, 3, 7, 3, 8, 3)
print("count of 3 :", tup_a.count(3)) # 4

print("Index of 8 :", tup_a.index(8)) # 5

# sorted function
result = tuple(sorted(tup_a))
print("result :", result)
# (3, 3, 3, 3, 6, 7, 8)

# reversed function
result2 = tuple(reversed(tup_a))
print("reverse result :", result2)

# (3, 8, 3, 7, 3, 6, 3)

print("_"*50)
######## Max, Min and sum function ##############
tup_q = (44, 55, 77, 11, 22, 78, 34, 9)

print("Max value :", max(tup_q)) # Max value : 78
print("Mini value :", min(tup_q)) # Mini value : 9
print("Sum value :", sum(tup_q)) # Sum value : 330


####################################
# program : write a python to calculate the factorial of all the given numbers.
tup_11 = (3, 6, 8, 5, 12, 4)
# output = factorials list
output = []

for val in tup_11:
    fact = 1
    for i in range(val, 0, -1):
        fact = fact*i

    output.append(fact)

print("Factorial output :", output)

