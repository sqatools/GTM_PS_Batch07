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