# (a-b)^2 = a^2+b^2-2ab


a = 50

b = 40

LHS = (a-b)**2

RHS = a**2 + b**2 - 2*a*b

print ("LHS : ", LHS) #LHS :  100

print ("RHS : ", RHS) #RHS :  100


print(LHS == RHS) #True


######################################################
# Radius of the circle

c = 100 # circumference

pi = 25/10

R = c/(2*pi)
print("Radius of the circle is ", R) #20.0

########################################################
# program to get simple interest

A =200000 # principle amount
B = 12# Number of years
C= 7 # Interest Rate

SI = (A*B*C)/120

print("Simple Interest is : ", SI) #140000.0

CI = A*(1+(R/100))**B - C

print ("Compound Interest is: ", CI) #1783213.0896511993
