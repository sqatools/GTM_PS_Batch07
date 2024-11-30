# (a-b)^2 = a^2+b^2-2ab

a = 15

b = 25

LHS = (a-b)**2

RHS = a**2 + b**2 - 2*a*b

print ("LHS : ", LHS)

print ("RHS : ", RHS)

print(LHS == RHS)

###################################################
# (a+b)^3 = a^3+b^3+3ab^2+3a^2b

LHS1 = (a+b)**3

RHS1 = a**3 + b**3 + 3*a*b**2 + 3*b*a**2

print("LHS1: ", LHS1)

print("RHS1 :", RHS1)

print(LHS1 == RHS1)

######################################################
# Radius of the circle

c = 88 # circumference
pi = 22/7

R = c/(2*pi)

print("Radius of the circle is ", R)

########################################################
# program to get simple interest

P = 100000 # principle amount
N = 5 # Number of years
R = 8 # Interest Rate

SI = (P*N*R)/100

print("Simple Interest is : ", SI)

CI = P*(1+(R/100))**N - P

print ("Compound Interest is: ", CI)