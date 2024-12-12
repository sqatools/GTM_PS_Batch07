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
