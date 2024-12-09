x = y = z = "Orange"
print(x)
print(y)
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print (y)
x=5
print(type(x))
print("*"*50)
num2 = 700
if num2%7 ==0:
    print ("The number can divide by 7:", num2)

str1 = "Python prog"
char = 'P'
if char in str1:
    print("Character is avilable in the string: ", char)
else:
    print("Character is not available in the string:", char)

    print("*"*50)

    num1 = 18
    if num1%2 == 0 and num1%3 ==0:
        print("The number is divisible by 2 and 3")
    else:
        print("The number is not divisible by 2 and 3")


print("-"*50)
l = [10,20,30,40]
b = bytes(l)
print(b)
for x in b:
    print(b)

print("-" * 50)
l = [255, 10, 20, 30, 40]
ba = bytearray(l)
ba[0] = 90
for x in ba:
    print(x)