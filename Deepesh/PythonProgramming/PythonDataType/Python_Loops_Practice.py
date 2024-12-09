for i in range(1, 11, 2):
    print(i)

print("_" *50)

# Get reverse value with negative different
for a in range(10, 1, -1):
    print(a)
print("_"*50)

# write a python programe to print the table of any input number
num = int(input("which table you want to print: "))
for i in range(1,11):
    print(i, "*", num, "=", i*num)
print("_"*50)

#apply if condition in the loop
#Get the number which are divisible by 3 and 5 between 1 to 50
for i in range (1,50):
    if i%3==0 and i%5==0:
        print(i)
    else:
        pass
print("_"*50)
# Finding the Factorial Number
num = int(input("Enter a Number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("The factorial of a number is : ", fact)
print("_"*50)
#Write a  Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
Input1:1500
Input2:2700
for i in range(1500, 2700+1):
    if i%7 == 0 *5:
        print(i)
''' Deepesh could you help me with above program'''