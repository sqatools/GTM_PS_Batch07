a = 30
# a : this is variable

# = : assingment operator
# 30 : value

print(a)
print(id(a))

# multiple variable with same valu
p = 500
q = 500

print("value of p :", p, id(p))
print("value of q :", q, id(q))

# If the variables values are same, then their memory address will be same.


#################################
# Assign one value to multiple variables
x = y = z = 100
print("value of x :", x)
print("value of y :", y)
print("value of z :", z)


########################################
# Assign multiple values to multiple variable at a time

p, q, r = 10, 20, 30

print("value of p :", p)
print("value of q :", q)
print("value of r :", r)




###########################################
# Rules to declare variable name.
# 1.  There should not be space in variable name

abc = 40 #correct
ab_pq = 50 #correct
Name = "Mohit" #correct


# var value = 500 # incorrect name, space is not allowed

# 2. Can not start variable name with numbers
var1 = 40 # correct
var_345_value_123 = 500 # correct
# 1var = 500 # incorrect name, can not start name with numbers


# 3. Varible name can not contain special character
# 3. Varible name can not contain special character
output_123 = 700  # correct
# output_value$ = 600 # incorrect, special character are not allowed in variable name


# 4. There is no limit to declare variable name
what_is_best_country_in_the_world = 'India'
fggswrfgwsedfgsssssssssssssssssssssssssssssssssssss= 'Hello'

# 5. Python variable names are case sensitive
name = 'Rahul'
Name = 'Mohit'
NaMe = 'Raju'
NAME = 'Shyam'
nAME = 'Raghu'


print("name :", name)
print("Name :", Name)
print("NaMe :", NaMe)
print("NAME :", NAME)
print("nAME :", nAME)



#################################################
#  Math operation with different math operators

"""
+ : plus operator
* : multiplication operator
- : minus operator
/ : division operator with single slace
//: division operator with double slace
% : remainder operator
** : Power operator
== : equal operator
!= : not equal to operator
"""

#addition of 2 values
num1 = 100
num2 = 200
num3 = num1 + num2
print("Addition of values :", num3)
print("Addition of values in console :", num1+num2)
# Addition of values in console : 300

# multiplication of 2 values
p1 = 4
q1 = 50
print("multiplication of p1 and q1 :", p1*q1)
# multiplication of p1 and q1 : 200


# Subtraction of values
X = 500
Y = 300
print("subtraction of values :", X-Y)
# subtraction of values : 200

# Division of values
A = 20
B = 3
C = 7

print("division with single / :", A/B)

# division of single / : 6.666666666666667
# when we divide any value with single slace then output will be pointer value or float data type

print("division with double // :", A//C)

# division with double // : 2
# When we divide any number with double //, then output will be a whole number or in int data type.

# % remainder operator operation
var1 = 20
var2 = 3
var3 = 4
print("remainder of 20 divide 3 :", var1%var2)#2
print("remainder of 20 divide 4 :", var1%var3)#0

# Get power value of any number
print("square of 2 :", 2**2) #4
print("cube of 4 :", 4**3) #64
print("square of 7 :", 7**2) #49

# compare variable values
var_a = 40
var_b = 50
var_c = 40

print(var_a == var_b) # False
print(var_a == var_c) # true
print(var_c != var_b # true


#############################################
# write a python program to solve quadratic equation
# (a+b)^2 = a^2 + b^2 + 2ab
a = 30
b = 12
LHS = (a+b)**2
print("LHS :", LHS)


RHS = a**2 + b**2 + 2*a*b
print("RHS output :", RHS)




