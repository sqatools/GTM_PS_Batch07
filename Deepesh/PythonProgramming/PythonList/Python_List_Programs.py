# program : write a list program to remove all the duplicated from given list
from Deepesh.PythonProgramming.PythonList.Python_List_Concepts import list_Y

list1 = [4, 6, 8, 4, 8, 2, 11, 5, 6]
# empty list
result = []

# apply loop to get each value
for val in list1:
    # check the value in the result list or not
    if val not in result:
        # if val not in result, then add in the list result
        result.append(val)
    else:
        # if val is already available in the list, then move next val
        continue

# print result
print("unique value :", result)
# [4, 6, 8, 2, 11, 5]


print("_"*50)
# program : Write a python program to get maximum value from given list

list2 = [4, 6, 8, 22, 55, 77, 33]
max_val = 0

for val in list2:
    if val > max_val:
        max_val = val
    else:
        continue

print("max value :", max_val)
# max value : 77


#programs :  write a python to find the all the prime numbers from given list
list3 = [2, 4, 19, 8, 7, 1, 11, 17]
result3 = []

# get each value from list3
for num in list3:
    # set prime flag as True
    prime = True
    # Check any number is divisible by the range of number from 2 to num
    for i in range(2, num):
        # if num is divisible by any value
        if num%i == 0:
            # Then set prime flag as False
            prime = False
            # break the inner loop
            break
        else:
            continue

    # If prime flag is still True for num value then add in result list
    if prime:
        result3.append(num)


print("result :", result3)
# [2, 19, 7, 1, 11, 17]

# program : write a python program provide the shopping bill amount from list of items purchased
list3 = [('tshirt', 300),
         ('lower', 400),
         ('Jeans', 1000),
         ('Jacket', 2000),
         ('Watch', 4000)]
# result provide the total bill amount

bill = 0
for val in list3:
    #print(val[1])
    bill = bill + val[1]

print("Bill amount :", bill)


# HW1 :  write a python program to second last max value from given list
list1 = [4, 6, 22, 77, 23, 44, 66, 100]
output = 77

# HW2 :  write a python program to move all positive value in left side of the list
# and negative to right side of the list
list2 = [4, 7, -2, 8, -11, 44, -7, -22]
# output = [4, 7, 8, 44, -2, -11, -7, -22]

print("-"*50)
############### append, insert #########
list_k = [2, 4, 6, 8, 9, 4,]
list_k.insert(-2, 300)
list_k.append(100)
list_k.append(500)
list_k.insert(2, 200)
list_k.insert(-2, 54)
print(list_k)

####### extend #####

list_l = [ "sar", 66, 43, 56, "fsd"]
list_m = ["tya", 44, 3543]
list_l.extend(list_m)
print(list_l)

list_m.extend(list_l)
print(list_m)

print("-"*50)

list_n = [4, 5, 6, 7, 7, 9]
list_o = ["sun", "moon", "dad", 5, 90, 123]
result6 = list_n + list_o
print(result6)
 # 4, 5, 6, 7, 7, 9, 'sun', 'moon', 'dad', 5, 90, 123]

###### multiply list #####

result7 = list_o*4
print(result7)
# ['sun', 'moon', 'dad', 5, 90, 123, 'sun', 'moon', 'dad', 5, 90, 123, 'sun', 'moon', 'dad', 5, 90, 123, 'sun', 'moon', 'dad', 5, 90, 123]

print("-"*50)

list_p = [76, 35, 87, 57, 87, 33, 56, 57, 33]
list_p.remove(87)
#
list_p.pop(-2)

print(list_p)
# [76, 35, 57, 87, 33, 56, 33]
pv1 = (list_p.pop())
print(pv1) # 33


print("-"*50)

list_q = [2, 4, 9, 7, 7, 10,8]
list_q.clear()
print(list_q) # []



list_r = [2, 4, 9, 7, 7, 10,8, 10, 7, 12, 13]
del list_r[3:5]
print(list_r)

print(list_r.count(10))
print(list_r.index(9))

print("-"*50)
####### sort ######

list_s = [67.0, 4., 345, 35, 35, 35, 2, 45, 22]
list_s.sort()
print(list_s)
# [2, 4.0, 22, 35, 35, 35, 45, 67.0, 345]
list_s.reverse()
print(list_s)
# [345, 67.0, 45, 35, 35, 35, 22, 4.0, 2]


reversed(list_s)
print(list_s)

print("-"*50)
##### sorted #######

list_t = [ 34, 54, 65, 12, 897,345, 768, 33243, 987,24323]

print(list(sorted(list_t)))
# [12, 34, 54, 65, 345, 768, 897, 987, 24323, 33243]
print(list(sorted(list_t, reverse=True)))
# [33243, 24323, 987, 897, 768, 345, 65, 54, 34, 12]
print(list_t)
# [34, 54, 65, 12, 897, 345, 768, 33243, 987, 24323]
print(sorted(list_t))
# [12, 34, 54, 65, 345, 768, 897, 987, 24323, 33243]


###### replace ########
print("-"*50)
list_v = [33, 44 ,55, 54, 76, 87]
list_v[3] = 56
print(list_v)
# [33, 44, 55, 56, 76, 87]

list_v[:2] = [52, 53, 54]
print(list_v)
# [52, 53, 54, 55, 56, 76, 87]

list_abc = [1, 2, 3, 4, 5]
list_abd = list_abc
list_abd.append(6)
print(list_abc)
# [1, 2, 3, 4, 5, 6]

list_y = ["a", "b", "c"]
list_z = list_y.copy()
list_z.append("d")
print(list_z)
# [1, 2, 3, 4, 5, 6]
print(list_y)
# ['a', 'b', 'c']






























##########################################################



print("_"*50)
# Program: write a  python program to find out all the palimdrome word from given string.
str_a = "Hello OPO We Are AAAoAAA Learning HellolleH Python"
word_list = str_a.split(" ")
print(word_list)
for word in word_list:
    # check for palimdrome word
    if word == word[::-1]:
        # print only palimdrome word
        print(word)
    else:
        continue

"""
OPO
AAAoAAA
HellolleH
"""


print("_"*50)
# write a python program to manage a fruit to calculate bill amount and update inventory
# [fruit_ name, fruit_stock, fruit_price]
fruit_items = [['Apple', 100, 20], ['Banana', 50, 10], ['Mango', 200, 75],
               ['Cherry', 150, 40], ['watermelon', 20, 100], ['PinaApple', 75, 150]]

cust_purchase_list = [['Apple', 5], ['Banana', 10], ['watermelon', 2]]
total_bill = 0

# 1. Calculate the bill
# 2. update inventory

for cust_item in cust_purchase_list:
    for stock_item in fruit_items:
        if cust_item[0] == stock_item[0]:
            # get fruit name from customer purchase
            fruit_name = cust_item[0]
            # calculate bill amount of each fruit
            fruit_bill = cust_item[1]*stock_item[2]
            # get updated the stock item value
            updated_stock = stock_item[1] - cust_item[1]
            # update the stock item value in the stock_item list
            stock_item[1] = updated_stock
            # add fruit item bill in total amount
            total_bill = total_bill + fruit_bill
            print(fruit_name, ":",cust_item[1],  ":", fruit_bill)

print("_"*50)
print("Total bill amount :", total_bill)

print(fruit_items)


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



