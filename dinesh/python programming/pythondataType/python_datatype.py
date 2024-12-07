"""
Python Data Type
1. Numbers
   i) Integer  ii) Float  iii) Complex number

2. Sequential
   i) String  ii) List  iii) Tuple

3. Dictionary
4. Set
5. Boolean
"""

##### Integer Data Type #####
var1 = 100
print(var1)
print(type(var1))
"""
->  Integer is immutable data type, once it defined we can not update the value.
->  Integer data type only consider whole number.
->  There is no limit for integer data type, we can defined any long value as integer.
->  Both positive and negative values will be consider as integer data.
"""

var2 = 200
var3 = 500
var4 = var2 + var3
print(var4)

var5 = 643564356943569435960843586953486905386
var6 = 0
var7 = -34343
print("var5 :", var5, type(var5))

print("var6 :", var6, type(var6))


print("var7 :", var7, type(var7))


print("_"*50)

########### Float data type ###############
var_a = 10.23
print(var_a, type(var_a))

"""
# Properties :
->  Float is immutable data type, once it is defined can not update
->  Float only consider the pointer values.
->  There is no limit for float data.
->  Both positive and negative values will be consider as float data.
"""

var_b = 0.23
var_c = 0.0
var_d = 4936322634564.56546564565445654
var_e = -50.33

print("var_b :", var_b, type(var_b))

print("var_c :", var_c, type(var_c))


print("var_d :", var_d, type(var_d))


print("var_e :", var_e, type(var_e))


print("_"*40)

################### Complex Number ####################
# x + yj
n1 = 30 + 40j
print(n1, type(n1))


print("real value :", n1.real)

print("imaginary value :", n1.imag)


num2 = 50 + 70j
num3 = 60 + 30j

num4 = num2 + num3
print("num4 :", num4)

######################### Sequential data type ###########

# String data type #
str1 = 'H'
str2 = "Hello"
str3 = ''' Hello we are learning Python Programs
Its fun work with python logic and easy to use
keywords.
'''
str4 = """
Hello
Python
Programming
"""
str5 = "345 ^&^&*^^ Hello PYTHON 50+70J"

print("str1 :", str1, type(str1))
print("+"*10)

print("str2 :", str2, type(str2))

print("+"*10)

print("str3 :", str3, type(str3))
"""
Hello we are learning Python Programs
Its fun work with python logic and easy to use
"""
print("+"*10)

print("str4 :", str4, type(str4))
print("+"*10)
"""
Hello
Python
Programming
 <class 'str'>
"""

print("str5 :", str5, type(str5))

print("+"*10)


str_a = "Hello"

"""
0   1   2   3   4   +ve
H   e   l   l   0
-5 -4  -3   -2  -1  -ve
"""

print(str_a[0])
print(str_a[-5])

str_b = "Python Programming"
print(str_b[7])
print(str_b[-5])

"""
# Properties of String 
-> String is a immutable data type.
-> Any character/word/sentence in single/double/triple quote, then will consider as string
-> String follows positive and negative indexing.
"""

var1 = 'Hello'
var1 = 'Python'
print(var1)

print("_"*50)

################### list data type ##########
list1 = [3, 3.5, 'Hello', [4, 6, 7]]
print(list1, type(list1))

"""
# Properties of list
->  list is a mutable data type, once it is defined we can modify or update values.
->  List can contains any type of data, int, float, string, list, tuple, dict, set, boolean
->  List Follows the positive and negative indexing.
->  List allows multiple type of operation, insert, remove, update, clear.
"""
print(dir(list))
"""
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

list1 = ['a', 'b', 'c', 'd', [4, 6, 7]]

print(list1[1])
print(list1[4])
print(list1[4][1])
print(list1[-1])
print(list1[-1][-1])

list2 = [4, 6, 8, 2, 12]
list2.append(100)
print("list2 :", list2)



print("_"*50)

########################## tuple data type ###########
tup1 = (4, 6, 8, 12, 4.5, 'Hello', [3, 5, 7])
print(tup1, type(tup1))

"""
# Properties:
->  tuple is immutable data type, once it is defined we can not change.
->  Tuple can contain all the types of data, int, float, string, list, dictionary, set, boolean
->  Tuple follows the position and negative indexing as like string and list
->  Tuple is faster than list in terms of performance.
->   Generally we use tuple data type, when data is not going to change further.
     e.g  ->  days in month
        ->  Days in week
"""

#       0   1          2             3
tup2 = (3, 'Python', 'Programming', 'Html')
#       -4  -3        -2              -1
print(tup2[3]) # Html
print(tup2[-3]) # Python

tup3 = (4, 4.5,
        [36, 63, 44, 34],
        'Hello',
        (4, 7, 9), {'a': 123, 'b' : 4567})

print("tup3 :", tup3)
print(tup3[2: 4])
# ([36, 63, 44, 34], 'Hello')
print("_"*50)

####################### Dictionary ##################################
# {'key' : 'value'}
var1 = {'a' : 123, 'b' : 456, 'c' : 445}
print(var1, type(var1))
# {'a': 123, 'b': 456, 'c': 445} <class 'dict'>

print(var1['b']) # 456

var1[123] = 500
var1['d'] = 1000
print(var1)

"""
# properties dictionary
->  Dict is mutable data type as like list, string
->  Dict only contains unique keys.
->  Dict allows only immutable data type as key e.g int, float, string, tuple, boolean'
->  Dict does not follow any indexing.
->  Dict can contains all of the data as value e.g. int, float, string, list, tuple, dict, set
"""

# We can get dictionary data, with help of keys.

dict2 = {'a' : 123, 'a': 455, 'b' : 456, 'c': 1000}
print(dict2)
print(dict2['a']) # 455

dict2['e'] = 600
print(dict2)
print(dir(dict))
print("_"*50)


##################### Set data type #######################
# set data only store unique data, duplicate values are not allowed in set
set1 = {4, 6, 8, 22, 44, 4, 6, 8}
print(set1)


"""
properties of set

->  Set is mutable data type
->  Set only contains unique data, duplicate values are not allowed.
->  Set does not follow any indexing
->  Set only contains immutable, int, float, string, tuple, boolean.
->  Dict, list and set is not allowed as member in the set.
->  Set store values in random order.
"""

#set2 = {4, 5.5, 'Hello', (3, 6, 8), True, False, {'a' : 234}}
#print(set2)
print(dir(set))
"""
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""

##################### Boolean data type ##################
"""
->  boolean data type consider only values True and False
->  boolean is immutable data type.'
->  boolean output will get with any condition program.
"""

var1 = True
print(var1, type(var1))