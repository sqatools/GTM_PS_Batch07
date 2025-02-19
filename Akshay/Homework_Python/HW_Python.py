# (a-b)^2 = a^2+b^2-2ab

a = 50

b = 40

LHS = (a-b)**2

RHS = a**2 + b**2 - 2*a*b

print ("LHS : ", LHS)

print ("RHS : ", RHS)

print(LHS == RHS)

###################################################
# (a+b)^3 = a^3+b^3+3ab^2+3a^2b

LHS0 = (a+b)**3

RHS1 = a**3 + b**3 + 3*a*b**3 + 3*b*a**3

print("LHS0: ", LHS0)

print("RHS1 :", RHS1)

print(LHS0 == RHS1)

######################################################
# Radius of the circle

c = 100 # circumference

pi = 22/7

R = c/(2*pi)
print("Radius of the circle is ", R)

########################################################
# program to get simple interest

A =200000 # principle amount
B = 12# Number of years
C= 7 # Interest Rate

SI = (A*B*C)/100

print("Simple Interest is : ", SI)

CI = A*(1+(C/100))**B - A

print ("Compound Interest is: ", CI)