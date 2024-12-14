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
