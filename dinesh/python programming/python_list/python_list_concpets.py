list_a = [4, 6, 8, 9]
list_a.append(200)
list_a.append(350)
print("list_a :", list_a)



############################################
#insert() method:
list_b = ['a', 'b', 'c', 'd', 'e']
list_b.insert(2, "F")
list_b.insert(-1, "z")
print("list_b ;", list_b)



####################################
#list concatenation() method :


list_e = [3, 6, 5, 4]
list_f = ['a', 'b', 'c', 'd']
list_g = ['A', 'B', 'C']

result = list_e + list_f + list_g
print("Resullt :", result)
##########################################
# multiply list values :

list_h = [4, 5, 9]
result2 = list_h*2
print("Result2 :", result2)
print("-"*50)
##########################################################
# write a python program to manage a fruit to calculate bill amount and update inventor
#[fruit_name, fruit_stock, fruit_price]

fruit_items = [['Apple', 100, 20], ['Banana', 50, 10], ['Mango', 200, 75],
               ['Cherry', 150, 40], ['watermelon', 20, 100], ['PinaApple', 75, 150]]

cust_purchase_list = [['Apple', 6], ['Banana', 12], ['watermelon', 7]]
total_bill = 0

for cust_item in cust_purchase_list:
    for stock_item in fruit_items:
        if cust_item[0] == stock_item[0]:
            fruit_name = cust_item[0]
            fruit_bill = cust_item[1] * stock_item[2]
            updated_stock = stock_item[1] - cust_item[1]
            stock_item[1] = updated_stock
            total_bill = total_bill + fruit_bill

            print(fruit_name, ":", cust_item[1], ":", fruit_bill)


print("_"*50)
print("Total bill amount :", total_bill)
print(fruit_items)
##Apple : 6 : 120
#Banana : 12 : 120
#watermelon : 7 : 700

#Total bill amount : 940
#[['Apple', 94, 20], ['Banana', 38, 10], ['Mango', 200, 75], ['Cherry', 150, 40], ['watermelon', 13, 100], ['PinaApple', 75, 150]]
############################################################
print("_"*50)

fruit_items = [['Apple', 100, 20], ['Banana', 50, 10], ['Mango', 200, 75],
               ['Cherry', 150, 40], ['watermelon', 20, 100], ['PinaApple', 75, 150]]

cust_purchase_list = [['Apple', 5], ['Banana', 10], ['Watermelon', 2]]
bill_amount = 0


for cust_item in cust_purchase_list:
    for stock_item in fruit_items:
        if cust_item[0] == stock_item[0]:
            fruit_name = cust_item[0]
            fruit_bill = cust_item[1]*stock_item[2]
            updated_stock = stock_item[1] - cust_item[1]
            stock_item[1] = updated_stock
            total_bill = total_bill + fruit_bill


            print(fruit_name, ":", cust_item[1], ":", fruit_bill)



print("total bill amount :", total_bill)
print("_"*50)

#############################ffvc########################


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


# 1. get employee details with employee ID

x = input("Enter the employee ID: ")
for i in employee_details :
    if i[0] == x :
        print("Employee Name: ", i[1])
        print("Employee email ID: ", i[2])
        print("Employee Location: ", i[3])
        print("Employee Phone Number: ", i[4])
        print("Employee Salary: ", i[5])

employee_details = [
    ['emp_123', 'rahul', 'rahul@gmail.com', 'Pune', 7897897987, 400000],
    ['emp_124', 'mohit', 'mohit@gmail.com', 'Pune', 5435345343, 500000],
    ['emp_125', 'pooja', 'pooja@gmail.com', 'Pune', 5435345432, 600000],
    ['emp_126', 'gourav', 'gourav@gmail.com', 'Pune', 4434543223, 700000],
    ['emp_127', 'sourav', 'sourav@gmail.com', 'Pune', 7897888886, 800000],
]


# 2. update employee details


y = input("Enter employee ID you want to update: ")
z = ['empid', 'Name', 'emailid', 'Location', 'Phone','Salary']

detail = input("Enter the employee detail you want to update: ")
update = input("Enter the updated detail: ")
for j in employee_details:
    for k in range(len(z)):
        if j[0] == y:
            if detail == z[k]:
                j[k] = update

print(employee_details)


# 3. Add new employee

employee_details = [
    ['emp_123', 'rahul', 'rahul@gmail.com', 'Pune', 7897897987, 400000],
    ['emp_124', 'mohit', 'mohit@gmail.com', 'Pune', 5435345343, 500000],
    ['emp_125', 'pooja', 'pooja@gmail.com', 'Pune', 5435345432, 600000],
    ['emp_126', 'gourav', 'gourav@gmail.com', 'Pune', 4434543223, 700000],
    ['emp_127', 'sourav', 'sourav@gmail.com', 'Pune', 7897888886, 800000],
]

Empid = input("Enter Employee ID: ")
Name = input("Enter Employee Name: ")
emailid = input("Enter Employee email ID: ")
Location = input("Enter Employee Location: ")
Phone = int(input("Enter Employee phone number: "))
Salary = int(input("Enter Employee Salary: "))

Newlist = [Empid, Name, emailid, Location, Phone, Salary]
employee_details.extend([Newlist])
print(employee_details)


# 4. removed employee details with employee ID.

employee_details = [
    ['emp_123', 'rahul', 'rahul@gmail.com', 'Pune', 7897897987, 400000],
    ['emp_124', 'mohit', 'mohit@gmail.com', 'Pune', 5435345343, 500000],
    ['emp_125', 'pooja', 'pooja@gmail.com', 'Pune', 5435345432, 600000],
    ['emp_126', 'gourav', 'gourav@gmail.com', 'Pune', 4434543223, 700000],
    ['emp_127', 'sourav', 'sourav@gmail.com', 'Pune', 7897888886, 800000],
]
r = input("Enter the Employee ID to remove details: ")
for i in employee_details:
    if i[0] == r:
        employee_details.remove(i)


print(employee_details)










