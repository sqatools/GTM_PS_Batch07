# write a python program to check given number is prime or not.
"""
num = int(input("Please enter the number :"))
count = 1
for val in range(2, (num//2+1)):
    print(val)
    if num%val == 0:
        count += 1
        break
    else:
        continue

if count > 1:
    print("This is not a prime number :", num)
else:
    print("This is a prime number :", num)
"""


# write a python program to get list of prime numbers from 1 to 100

for num in range(2, 100):
    count = 1
    for val in range(2, (num//2+1)):
        #print(val)
        if num%val == 0:
            count += 1
            break
        else:
            continue

    if count == 1:
        print(num)
