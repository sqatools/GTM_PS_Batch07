x = input("Enter your age: ")
x = int(x)
if x >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

a = input("Enter a value: ")
a = int(a)
if a%2 == 0:
    print ("The square of the value is: ", a**2)
elif a%3 == 0:
    print ("The cube of the value is: ", a**3)
else:
    print("The value is not divisible by 2 or 3")