list1 = [2, 3.4, (3, 7, 1), {'a': 23, 'b': 456}, True]
print(list1, type(list1))
print("_" * 50)

# HW : Write a Python Program to create a employee management system with the help of list structure.

employee_details = [
    ['emp_123', 'rahul', 'rahul@gmail.com', 'Pune', 7897897987, 400000],
    ['emp_124', 'mohit', 'mohit@gmail.com', 'Pune', 543534534, 500000],
    ['emp_125', 'pooja', 'pooja@gmail.com', 'Pune', 543534543, 600000],
    ['emp_126', 'gourav', 'gourav@gmail.com', 'Pune', 443454322, 700000],
    ['emp_127', 'sourav', 'sourav@gmail.com', 'Pune', 789788888, 800000],
]


# 1. get employee details with employee ID
def get_employee_details(emp_id):
    for emp in employee_details:
        if emp[0] == emp_id:
            return emp
    return "Employee not found"


print(get_employee_details('emp_123'))
print("_" * 50)


# 2. update employee details
def update_employee_details(emp_id, updated_details):
    for emp in employee_details:
        if emp[0] == emp_id:
            emp[1] == updated_details.get('name', emp[1])
            emp[2] == updated_details.get('email', emp[2])
            emp[3] == updated_details.get('location', emp[3])
            emp[4] == updated_details.get('phone', emp[4])
            emp[5] == updated_details.get('salary', emp[5])
            return f"Employee {emp_id} details updated successfully."
        return "Employee not found"


print(update_employee_details('emp124', {'name': 'Mohit sharma', 'salary': 550000}))
print("_" * 50)


# 3. Add new employee
def add_new_employee(emp_details):
    employee_details.append(emp_details)
    return "New employee added successfully"


print(add_new_employee(['emp_128', 'amit', 'amit@gmail.com', 'Mumbai', 1122334455, 450000]))
print("_"*50)


# 4. removed employee details with employee ID.
def remove_employee(emp_id):
    for emp in employee_details:
        if emp[0] == emp_id:
            employee_details.remove(emp)
            return f"Employee {emp_id} removed successfully"


print(remove_employee('emp_126'))
print(employee_details)
