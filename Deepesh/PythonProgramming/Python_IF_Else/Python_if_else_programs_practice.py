"""
1.  If-else

if cond:
    code1
else:
    code2
"""


# write a python program to check given number is even or odd
num=21

if num%2 == 0:
    print("The number is even")
else:
    print("The number is odd")

print("_"*50)
# check given number is divisible by 3 and 5
num1 = 15
if num1%3 == 0 and num1%5 == 0:
    print("The number is divisible by 3 and 5")
else:
    print("The number is not divisible 3 and 5")


"""
2. 

if cond1:
    code1
elif cond2:
    code2
elif cond3:
    code3

"""

# write a python program to calculate the eletricity bill as per the consumtion
total_unit = -201
#total_bill = 0

if 0 < total_unit <= 100:
    total_bill = total_unit*10
    print("Total bill amount :", total_bill)

elif 100 <= total_unit <= 200:
    total_bill= total_unit*15
    print("Total bill amount :", total_bill)

elif total_unit > 200:
    total_bill = total_unit*20
    print("Total bill amount :", total_bill)
else:
    print("not applicable, unit number should be positive")


"""
3. Nested If condition.

if cond1:  # main door
    code1
    if cond2:  # kitchen door
        code
        if cond3 #  fridge door
            code
        else:
            code
            
    else:
        code
    
else:
    code1

"""
print("_"*50)

main_door = 'open'
kitchen_door = 'open'
fridge_door = 'close'

if main_door == "open":
    print("Welcome to home")
    if kitchen_door == "open":
        print("Welcome to home kitchen, enjoy your feast")
        if fridge_door == "open":
            print("Please enjoy the Ice Cream")

        else:
            print("Kids are not allowed open fridge")
    else:
        print("Sorry, you are guest, not allowed in the kitchen")
else:
    print("Sorry, not allowed in the home")



user_list1 = ['id_01', 'id_02', 'id_03']
user_id = 'id_03'

if user_id in user_list1:
    print("Valid user")
else:
    print("Invalid user")
