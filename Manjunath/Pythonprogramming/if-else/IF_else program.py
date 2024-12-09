
#### Check the number is divisible by 3 ####
numa = 21
if numa%3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")

#### If-else program to assign grades as per total marks ####
print("_"*70)
marks = 60
if marks<40:
    print("Fail")
elif marks>=40 and marks<=50:
    print("GraDe C")
elif marks>=50 and marks<=60:
    print("GraDe B")
elif marks>=60 and marks<=70:
    print("GraDe A")
elif marks>=70 and marks<=80:
    print("GraDe A+")
elif marks>=80 and marks<=90:
    print("GraDe A++")
elif marks>=90 and marks<=100:
    print("Excellent")
else:
    print("Inavlid marks")


#### Python program to check number is divided by 3 and 5 ####
print("_"*50)
numb = 15
if numb%3==0 and numb%5==0:
    print("Given number is  divided by 3 and 5")
else:
    print("Given number cant be divided by 3 and 5")

#### Python program to print the square of the number ####
print('_'*50)
var =  33
if var%11 == 0:
    print(var**2)
else:
    print("Number is not divisible by 11")

    print("It is a prime number")

####Program to check whether the number is odd or even ####
print('_'*50)
numd =  12
if numd%2 == 0:
   print("It is an even number")
else:
   print("It is an odd number")

####Fibonacci series####
print('_'*50)
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
numE = 13
if numE in fib:
    print("It is a part of the series")
else:
    print("It is not a part of the series")

###authentication of username and password####
print('_'*50)
Uname = "EPOSAudio"
password = "EPOSAudio"
if Uname == password:
    print("It is valid")
else:
    print("It is not valid")

###validate user_id in the list of user_ids####
print('_'*50)
id_list = [10,20,30,50,60,70,80]
id_ = 50
if id_ in id_list:
    print("Valid ID")
else:
    print("Invalid ID")

###Print a square or cube of the given number####
print('_'*50)
num1 = 14
if num1%2 == 0:
   print("Sqaure: ",num1**2)
elif num1%3 == 0:
   print("Cube: ",num1**3)


####Python nested If else program to describe the interview process###
print('_'*50)
#round1 = input("Enter round1 result:")
#round2 = input("Enter round2 result:")
round1 = "Passed"
round2 = "Passed"
if round1 == "Passed":
    print("congrats you have been selected for round2")
    if round2 == "Passed":
           print("Congrats you are selected")
    else:
           print("round 2 failed, better luck next time")
else:
    print("failed in round1 , try next time")


#####Determine whether a number is available in the list###
print('_'*50)
list_a = [11,22,33,44,55,66,99,88,77]
num_a  = 99
if num_a in list_a:
    print(f"{num_a} Value in the list")
else:
    print(f"{num_a} Value is not in list")

####Find the largest number among three numbers #####
print('_'*50)
num_x = 45
num_y = 55
num_z = 15
if num_x>num_y:
    if num_x>num_z:
        print(f"{num_x} is the greatest")
    else:
        print(f"{num_z} is the greatest")
else:
    if num_y>num_z:
        print(f"{num_y} is the greatest")
    else:
        print(f"{num_z} is the greatest")


######
