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
print(type(var1))  # <class 'int'>
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
# 643564356943569435960843586953486905386 <class 'int'>

print("var6 :", var6, type(var6))
#  0 <class 'int'>

print("var7 :", var7, type(var7))
# -34343 <class 'int'>


print("_"*50)
############ Float data type ###############
var_a = 10.23
print(var_a, type(var_a))
# 10.23 <class 'float'>

"""
# Properties :
->  Float is immutable data type, once it is defined can not update
->  Float only consider the pointer values.
->  There is no limit for float data.
->  Both positive and negative values will be consider as float data.
"""

var_b = 0.23
var_c = 0.0
var_d = 4936322634564.56546564565445654  #
var_e = -50.33

print("var_b :", var_b, type(var_b))
# 0.23 <class 'float'>

print("var_c :", var_c, type(var_c))
# 0.0 <class 'float'>

print("var_d :", var_d, type(var_d))
# 4936322634564.565 <class 'float'>

print("var_e :", var_e, type(var_e))
# -50.33 <class 'float'>



print("_"*40)
################### Complex Number ####################
# x + yj
n1 = 30 + 40j
print(n1, type(n1))

# (30+40j) <class 'complex'>
print("real value :", n1.real)
# real value : 30.0

print("imaginary value :", n1.imag)
# imaginary value : 40.0

num2 = 50 + 70j
num3 = 60 + 30j

num4 = num2 + num3
print("num4 :", num4)  # (110+100j)

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
print("+"*10)  # H <class 'str'>

print("str2 :", str2, type(str2))
# Hello <class 'str'>
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
# 345 ^&^&*^^ Hello PYTHON 50+70J <class 'str'>
print("+"*10)

# String Follows positive and negative index
str_a = "Hello"

"""
0   1   2   3   4   +ve
H   e   l   l   0
-5 -4  -3   -2  -1  -ve
"""

print(str_a[0]) # H
print(str_a[-5]) # H

str_b = "Python Programming"
print(str_b[7])  # P
print(str_b[-5]) # m

"""
# Properties of String 
-> String is a immutable data type.
-> Any character/word/sentence in single/double/triple quote, then will consider as string
-> String follows positive and negative indexing.
"""

var1 = 'Hello'
var1 = 'Python'
print(var1)

