# HOME WORK
"""
1. (a-b)^2
2. (a+b)^3
3. program to get radius of circle
4. program to get simple interest
5. program to get compound interest
"""
#1. (a-b)^2
a=10
b=5
c=(a-b)**2
print("1.The value of c =",c)

#2. (a+b)^3
a=20
b=10
c=(a+b)**3
print("2.The value of c=",c)

#3. program to get radius of circle
#Formula for radius of circle =R = c/(2*pi)
pi=22/7
c=50
R= c/(2*pi)

print("3.Radius of the circle R =",R)

#4. program to get simple interest
#formula of simple interest :SI = (P*N*R)/100

P=20
R=5
N=6
SI = (P*N*R)/100

print("4.The value of simple interest",SI)

#5. program to get compound interest
#formula of compound interest:CI = P*(1+(R/100))**N - P
CI = P*(1+(R/100))**N - P
print("5.The value of compound interest",CI)
