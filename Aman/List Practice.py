list3 = [('tshirt', 300),
         ('lower', 400),
         ('Jeans', 1000),
         ('Jacket', 2000),
         ('Watch', 4000)]

print("Total Bill Amount:", sum(price for item, price in list3))

print("_"*50)

# HW1 :  write a python program to second last max value from given list


# output = 77

list1 = [4, 6, 22, 77, 23, 44, 66, 100]
max_val = 0
second_max = 0
for val in list1:
    if val > max_val:
        second_max = max_val
        max_val = val
    elif val > second_max and val != max_val:
        second_max = val
print("Largest value:", max_val)
print("Second largest value:", second_max)


# HW : Write a Python Program to create a employee management system with the help of list structure.

employee_details = [
    ['emp_123', 'rahul', 'rahul@gmail.com', 'Pune', 7897897987, 400000],
    ['emp_124', 'mohit', 'mohit@gmail.com', 'Pune', 543534534, 500000],
    ['emp_125', 'pooja', 'pooja@gmail.com', 'Pune', 543534543, 600000],
    ['emp_126', 'gourav', 'gourav@gmail.com', 'Pune', 443454322, 700000],
    ['emp_127', 'sourav', 'sourav@gmail.com', 'Pune', 789788888, 800000],
]
# 1. get employee details with employee ID
# 2. update employee details
# 3. Add new employee
# 4. removed employee details with employee ID.

# 1. Get Employee Details by Employee ID

emp_id = 'emp_125'
emp_found = None
for emp in employee_details:
    if emp[0] == emp_id:
        emp_found = emp
        break
if emp_found:
    print("Employee Details:", emp_found)
else:
    print("Employee not found.")

print("_"*50)

dict_2 = {'a': [3, 5, 7, 8],
        'b': [2, 6, 8, 9],
        'c': [1, 4, 7, 8]}

for key in dict_2:
    print(f"Sum of {key}: {sum(dict_2[key])}")

for key in dict_2:
    print(f"Average of {key}: {sum(dict_2[key]) / len(dict_2[key])}")
