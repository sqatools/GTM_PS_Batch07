print ("hello")

for i in range(1, 5):
    for j in range(i):
        print(j)

print("_"*50)
for i in range(1, 5):
    for j in range(i):
        print(i, end='')
        i+= 1

print("_"*50)

satya1 = 230
if satya1%2 == 0:
    print("satya1 is even number", satya1)
else:
    print("satya1 is odd number", satya1)

print("_"*50)

num1 = 350
if num1%2 == 0 and num1%5 == 0:
    print("num1 is devided by 2 and 5 :", num1)
else:
    print("num1 is not divided by 2 and 5:", num1)

print("_"*50)

num1 = 352
if num1%2 == 0 or num1%5 == 0:
    print("num1 is devided by 2 and 5 :", num1)
else:
    print("num1 is not divided by 2 and 5:", num1)

print("_"*50)

units = 1200
bill = 0

if 0 < units <= 100:
    bill = units*10
    print("current bill :", bill)
elif 100 < units <= 150:
    bill = units*12
    print("current bill :", bill)
elif 150 < units <= 200:
    bill = units * 15
    print("current bill :", bill)
elif units > 200:
    bill = units*20
    print(bill)

print("_"*50)

marks = 76

if 500 < marks <= 600:
    print("student got D grade :", marks)
elif 600< marks <= 650:
    print("student got C grade :", marks)
elif 650< marks <= 720:
    print("student got B grade :", marks)
elif marks > 720:
    print(" A grade :", marks)
else :
    print("Failed :", marks)


# print("_"*50)
# # 1). Python program to check given number is divided by 3 or not.
#
# num_a = 97
# if num_a%3 == 0:
#     print("num_a :", num_a)
# else:
#     print("number is not divided by ;", num_a)
#
# print("_" * 50)
# # 2). If else program to get all the numbers divided by 3 from 1 to 30.
#
# for i in range(1, 30):
#     if i%3 == 0:
#         print(i, end=' ')

print("_" * 50)
#3). If else program to assign grades as per total marks.

# marks = int(input("enter number"))
#
# if marks < 40:
#     print("fail")
# elif 40<= marks <= 50:
#     print("grade C :", marks)
# elif 50 < marks <= 60:
#     print("grade B :", marks)
# elif 60 < marks <= 70:
#     print("grade A :", marks)
# elif 70 < marks <= 80:
#     print("grade A+ :", marks)
# elif 80 < marks <= 90:
#     print("grade A++ :", marks)
# elif 90 < marks <= 100:
#     print("Excellent :", marks)
# else:
#     print("invalid marks :", marks)


# 4). Python program to check the given number divided by 3 and 5.
#
# print("-"*50)
#
# num_c = int(input("please enter num"))
#
# if num_c%3 == 0 and num_c%5 == 0:
#     print("number is devided by 3 and 5 :", num_c)
# else:
#     print("number is not divided by 3 and 5 :", num_c)
#
# print("-"*50)
# # 5). Python program to print the square of the number if it is divided by 11.
#
# num_d = int(input("enter number"))
#
# if num_d%11 == 0:
#     print(num_d**2)
# else:
#     print("number is not divisible")

#
#
# print("-"*50)
# # 7). Python program to check given number is odd or even.
#
# num_e = int(input("enter"))
#
# if num_e%2 == 0:
#     print("even number :", num_e)
# else :
#     print("odd number :", num_e)


# 8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
#
# print("-"*50)
#
# fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# num = int(input("number please"))
#
# if num in fib:
#     print("it is a part of fibonacci series")
# else:
#     print("not is the series")


# 9). Python program to check authentication with the given username and password.
# print("-"*50)
#
# username = str(input("please enter username"))
# password = str(input("plese enter the password"))
#
# if username == 'satya':
#     if password == "9490570891":
#         print("login sucessful")
#     else:
#         print("wrong password")
# else:
#     print("wrong username")


print("-"*50)

correct_user = "ramki"
correct_password = "8500631022"

username = input("enter username")
password = input("enter password")

if username == correct_user and password == correct_password:
    print("login sucessfull")
elif username != correct_user:
    print("username is wrong")
elif password != correct_password:
    print("wrong password")
elif username != correct_user and password != correct_password:
    print("both are wrong")




