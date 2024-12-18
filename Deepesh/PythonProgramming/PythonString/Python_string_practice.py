str1 = "Good MOrnInG"
print(str1, type(str1))

# Good MOrnInG <class 'str'>
print(str1[5]) # M
print(str1[-3]) # I
print(str1[3]) # d
print(str1[8]) # n

########### String Formatting #######

Name = "Mohit"
Age = 25
City = "Mumbai"

# Hello My Name is Mohit and age is 25, I live in mumbai

# 1. String concatenation
result1 = "Hello My Name is "+Name+" and age is "+str(Age)+", I live in "+City
print(result1)

# 2 Format method:
result2 = "Hello My Name is {} and age is {}, I live in {}".format(Name, Age, City)
print(result2)

# 3. fstring formatting.
result3 = f"Hello My Name is {Name} and age is {Age}, I live in {City}"
print(result3)

var1 = "Hello"
var2 = "Good Morning"
print(var1 +" "+var2)  # Hello Good Morning
print(f"{var1} {var2}") # Hello Good Morning

print("_"*50)
############ Convert string into raw string ##########
# Use r before double/single quote to convert the string into raw string.
str_a = r"India Is \t Going to Play \n\n Third Test With \t Ausis on 14th"
print(str_a)

print("_"*50)
############ Apply loop on the string ##########
str_b = "Python Programming"

### without index ###
for char in str_b:
    print(char, end=" ")
# P y t h o n   P r o g r a m m i n g

### with indexing ####

str_len = len(str_b)
print(str_len) # 18
for i in range(str_len):
    #print(i, str_b[i])
    print(str_b[i], end=" ")



print("_"*50)
#### ASCII RANGE OF CHARACTERS ###
# capital letter : 65-90
# small letter :   97-122

# ord function return the ASCII value with the help of character
print(ord('A')) # 65
print(ord('Z')) # 90

print(ord('a')) # 97
print(ord('z')) # 122

# chr function return the character with the help of ASCII value.
for i in range(65, 91):
    print(chr(i), end=" ")
"""
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
"""

for i in range(97, 123):
    print(chr(i), end=" ")

# a b c d e f g h i j k l m n o p q r s t u v w x y z

print()
################ String Slicing ###################
print("_"*50)
# Rule1 : str[initial index : last index]
# Result substring will include initial index character and exclude the last index.
# The substring result will always get from left to right

str_c = "Python Programming"
print(str_c[0:6]) # Python

print(str_c[-11:-1]) # Programmin

# when we don't define the last index, then default last index will be end of the string
print(str_c[-11:])  # Programming

print(str_c[2:-7])  # thon Prog

# right to left movement is not possible
print(str_c[-2:5])  # Blank Output

# if don't defined any initial index, then default initial index is 0
print(str_c[:8])  # Python P
print(str_c[:-2]) # Python Programmi

# print string except first and last character
print(str_c[1:-1]) # ython Programmin

#                   -30      19 -19   30
str_d = "Very good evening, hope you are doing good"
print(str_d[-19:30])


print("_"*50)
######## Rule2 str[initial_index:last_index: difference]  #######
str_e = "We are Learning Program"

print(str_e[2: 15: 1])  #  are Learning
print(str_e[2: 15: 2])

# r erig

print(str_e[-3:-20: -1])#  rgorP gninraeL er

#Q1: write a python program to solve this probml
str1 = "Virat is best India Player"
#. 1 print all value except first and last
#. output =  "irat is best India Playe"

# output2 =  "VViratt iiss bbestt IIndiaa PPlayerr"
result1 = str1[1:-1]
print(result1)

# Q2:
w1 = str1[0:5]
w2 = str1[6:8]
w3 = str1[9:13]
w4 = str1[14:19]
w5 = str1[20:]

W1 = f"{w1[0]}{w1}{w1[-1]}"
W2 = f"{w2[0]}{w2}{w2[-1]}"
W3 = f"{w3[0]}{w3}{w3[-1]}"
W4 = f"{w4[0]}{w4}{w4[-1]}"
W5 = f"{w5[0]}{w5}{w5[-1]}"
result2 = f"{W1} {W2} {W3} {W4} {W5}"
print(result2)

print("_"*50)
#############################################
# Rul3 str[:last index: difference]
#1. If difference is positive then default initial index will be zero
#2. If difference is negative the defailt initial index will be -1

str1 = "Good Morning"

# default initial index is zero as difference is positive
print(str1[:8:1])  #Good Mor

# default initial index is -1 as difference value is negative
print(str1[:5:-1]) # gninro

print(str1[:-6:1]) # Good M

print(str1[:-6:-1]) # gninr


print("_"*50)
###################################################
# RulE4 : str[:: difference]
# 1. If difference is positive then default initial index will be zero and last index
#    will be end of the string.

#2.  If difference is negative then default initial index will be -1 and last index will
#    will be begining of string

str_a = "Learning Is Fun"
print(str_a[::2])  # Lann sFn

print(str_a[::-1]) # nuF sI gninraeL

# Home work

# str1 = "We are learning Python Programming"
# 1. swap first and last character of each word
# result1 = "eW era gearninl nythoP  grogramminP"

# 2. Reverse each word of the string.
# output = "eW era gninrael nohtyP  gnimmargorP"


# string home work
str1 = "We are learning Python Programming"
w1 = str1[0:2]
w2= str1[3:6]
w3 = str1[7:15]
w4 = str1[16:22]
w5 = str1[23:]

print(w1, ":", w2, ":", w3, ":", w4, ":",w5)
W1 = f"{w1[-1]}{w1[0]}"
print(W1)
W2 = f"{w2[-1]}{w2[1]}{w2[0]}"
print(W2)
W3 = f"{w3[-1]}{w3[1:-1]}{w3[0]}"
W4 = f"{w4[-1]}{w4[1:-1]}{w4[0]}"
W5 = f"{w5[-1]}{w5[1:-1]}{w5[0]}"

result1 = f"{W1} {W2} {W3} {W4} {W5}"
print(result1)

# Reverse each word of the string.
M1 = w1[::-1]
M2 = w2[::-1]
M3 = w3[::-1]
M4 = w4[::-1]
M5 = w5[::-1]
result2 = f"{M1} {M2} {M3} {M4} {M5}"
print("Result2 :", result2)

print("_"*50)
########################## Python String Methods ###############
print(dir(str))

"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
  'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

#########
# upper() and lower() method: These method convert upper case string to lower case
#         and lower case string to upper case

str_a = "Hello We Are Learning PYthon Programming"
print(str_a.upper())
# HELLO WE ARE LEARNING PYTHON PROGRAMMING

print(str_a.lower())
# hello we are learning python programming

print(str_a[6].lower())

print("_"*50)
######
# islower() and isupper() Method:
# These methods check the given string is in lower case or upper case

str_e = "HELLO GOOD MORNING"
str_f = "good evening"
print("is upper check str_e:", str_e.isupper()) # True
print("is lower check str_e:", str_e.islower()) # False
print("is lower check str_f:", str_f.islower()) # True

print("_"*50)
################
# title() and istitle method:
# title method convert first letter of each word into camel case and istitle check the given string
# follows the rule of title sentence.
str_g = "HeY hope yoU Are DOing Good"
print("str_g :", str_g.title())
output = str_g.title()
# Hey Hope You Are Doing Good

print("Istitle for str_g :", str_g.istitle())  # False
print("istitle for output :", output.istitle())  # True

print("_"*50)
################
# Replace Method: Replace method helps to update any character or substring in the given string.
str_b = "Hello We Are Learning PYthon Programming"
str_c = str_b.replace("W", "w")
print(str_c)

str_d = str_b.replace("PYthon", "JAVA")
print(str_d)


print("_"*50)
# ################
#  count() Method: This method count the occurrences of any character or substring in the given string

str_j = "Lets Hope India will win the last Test India Match"
print("count of l :", str_j.count("l")) # 3
print("Count of India :", str_j.count("India")) # 2

Total_character = len(str_j)
print("Total character :", Total_character) # Total character : 50



print("_"*50)
# ################
#  swapcase() Method: This method covert all the character from Upper to lower and lower to upper.
str_k = "Lets HopE IndIa wiLL win the last Test India Match"
print("swap case of str_k :", str_k.swapcase())
# lETS hOPe iNDiA WIll WIN THE LAST tEST iNDIA mATCH


print("_"*50)
# Write a python program to get count of each character in the string.
str_l = "Lets HopE IndIa wiLL win the last Test India Match"
temp = "" # empty

# loop over input string
for char in str_l:
    # check char is not in temp variable
    if char not in temp:
        # print the character and its count
        print(char, str_l.count(char))
        # add character to temp variable
        temp = temp + char
    else:
        # continue if the character is repeated.
        continue


print("_"*50)
# ################
#  index() Method : This method return the index position of available sub-string or character.
str_x = "Good Morning"
print("index of M :", str_x.index("M")) # 5
print("index of ing :", str_x.index("ing")) # 9

# find the index of un-available string
# print("index of ing :", str_x.index("MM")) # 9
# It gives error and fail the program if the target sub-string in not available
# ValueError: substring not found


print("_"*50)
############
# find method : This method return the index position of character or sub-string if it is available or
#               method will return -1 if the sub-string/character is not available

str_q = "Hello Python Programming"
print(str_q.find("Python")) # 6

# output of not available data is expected  value -1
print(str_q.find("Good")) # -1



print("_"*50)
############
# split method: This method split the string with given delimeters or substring and return the list of words.

str_p = "Python#Programming#Is#Easy#To#Learn"
# split the string with #
result = str_p.split("#")
print("split result  :", result)
# ['Python', 'Programming', 'Is', 'Easy', 'To', 'Learn']

str_p = "Good Morning Learning is Fun"
# split the string with space
result2 = str_p.split(" ")
print(result2)
# ['Good', 'Morning', 'Learning', 'is', 'Fun']




print("_"*50)
############
# strip method : This method helps to remove trailing spaces from given string.
# Trailing space means, spaces that are available in the begining and end of string.

str_c = "  Python Programming  "
print(str_c)
result1 = str_c.strip()
print(result1)

# remove right side space
print(str_c.rstrip())

# remove left side space
print(str_c.lstrip())


print("_"*50)
############
# join() method : This help to join string with any word/character/number/special character

str_d = "Programming"

result = "-".join(str_d)
print("join result :", result) # P-r-o-g-r-a-m-m-i-n-g

result2 = "%$^$#".join(str_d)
print("join result2 :", result2) # P%$^$#r%$^$#o%$^$#g%$^$#r%$^$#a%$^$#m%$^$#m%$^$#i%$^$#n%$^$#g

print("_"*50)
##########################
# isnumeric method : This method check the given string only contains numbers

str_t = "67887678"
str_k = "2432 Hello"
print("Check all the values are numeric  str_t :", str_t.isnumeric()) # True
print("Check all the values are numeric str_k :", str_k.isnumeric()) # False

#isalpha : This method check the target string contains only alhabates.

str_a = "Hello"
str_b = "Python 123"

print("check alphabtes str_a :", str_a.isalpha()) # True
print("check alphabtes str_b :", str_b.isalpha()) # False

# isalnum : This method check the given string contains alphanumeric value
str_p = "Python123"
str_q = "Hello 345"
print("str_p contains alphanumeric value :", str_p.isalnum()) # True
print("str_q contains alphanumeric value :", str_q.isalnum()) # False

#isspace : This method return true if string only contains space.
str_x = "   "
str_y = "H E L L O"
print("set_x is contains space  :", str_x.isspace()) # True
print("set_y is contains space  :", str_y.isspace()) # False
