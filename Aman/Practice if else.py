print("Hello world")


def check_voting_permission():
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You have voting permission.")
    else:
        print("You do not have voting permission.")


def math_operations():
    value = int(input("Enter a number: "))

    if value % 2 == 0:
        print(f"Square of {value} is: {value ** 2}")
    elif value % 3 == 0:
        print(f"Cube of {value} is: {value ** 3}")
    else:
        print("Number is neither divisible by 2 nor 3")

# 1. Check if a number is divisible by 3
num = int(input("Enter a number: "))
if num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 3")

# 2. Numbers divisible by 3 from 1 to 30
for i in range(1, 31):
    if i % 3 == 0:
        print(i)

# 3. Assign grades based on marks
marks = int(input("Enter marks: "))
if marks > 100:
    print("Invalid marks")
else:
    if marks > 90:
        print("Grade Excellent")
    elif marks > 80:
        print("Grade A++")
    elif marks > 70:
        print("Grade A+")
    elif marks > 60:
        print("Grade A")
    elif marks > 50:
        print("Grade B")
    elif marks > 40:
        print("Grade C")
    else:
        print("Fail")

# 4. Check if a number is divisible by both 3 and 5
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

# 5. Print square if divisible by 11
num = int(input("Enter a number: "))
if num % 11 == 0:
    print("Square:", num * num)

# 6. Check if a number is prime
num = int(input("Enter a number: "))
if num > 1:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
else:
    print("Not a prime number")

# 7. Check if a number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 8. Check if a number is in Fibonacci series from 1 to 10
num = int(input("Enter a number: "))
fibonacci = [1, 1, 2, 3, 5, 8]
if num in fibonacci:
    print("Number is in Fibonacci series")
else:
    print("Number is not in Fibonacci series")

# 14. Largest among three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b:
    if a > c:
        print("Largest:", a)
    else:
        print("Largest:", c)
else:
    if b > c:
        print("Largest:", b)
    else:
        print("Largest:", c)

# 15. Check voting eligibility
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 16. Check if a number is a palindrome
num = input("Enter a number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# 17. Check if a string is a palindrome
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


