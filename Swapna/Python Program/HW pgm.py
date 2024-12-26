# #4. Write a python program to get email and phone number from given string
#
# str1 = " Hello python 8989898787 test@gail.com 5654645645 user2@tahoo.com Hope doing good"
#
# word_list = str1.split(" ")
# print(word_list)
#
# phone_numbers = []
# emails = []
#
# # for word in word_list:
# #     if word.isdigit() and len(word) == 10:
# #         phone_numbers.append(word)
# #     elif  '@' in word and ".com" in  word :
# #         emails.append(word)
# #
# #
# #
# # print("phone number : ", phone_numbers)
# # print(" emails", emails)
#
# for word in word_list:
#     if word.isnumeric and len(word)==10:
#         print(word)
#     elif '@' in word and ".com" in word:
#         print(word)
#
#
#
# print("phone number : ", phone_numbers)
# print(" emails", emails)
#
#
# str_p = "Hello We Are Learning Python"
# output = "Python"
# maxlen = 0
# nextlen = 0
# longword = ""
# nextword = ""
# wordlist = str_p.split(" ")
#
# for word in wordlist:
#     wordlen = len(word)
#     if wordlen > maxlen:
#         maxlen = wordlen
#         longword = word
#     elif maxlen > wordlen >nextlen:
#         nextlen = wordlen
#         nextword = word
#
# print("Second longest word: ", nextword)


# HW1 :  write a python program to second last max value from given list
# list1 = [4, 6, 22, 77, 23, 44, 66, 100]
# output = 77
#
#
# largest_num = 0
# seclarge_num = 0
# for val in list1:
#     if val > largest_num:
#         seclarge_num =largest_num
#         largest_num = val
#
#     if val < largest_num and val > seclarge_num:
#         seclarge_num = val
#
#
# print("seclarge num", seclarge_num)

# HW2 :  write a python program to move all positive value in left side of the list
# and negative to right side of the list

# output = [4, 7, 8, 44, -2, -11, -7, -22]

# l = [4, 7, -2, 8, -11, 44, -7, -22]
#
# n = len(l)
# print(" orginal list", l)
#
# for i in range(n-1):
#      for j in range(n-i-1):
#           if l [ j ] <0:
#                 l [ j ], l [ j + 1] = l [ j + 1], l [ j ]
#
# print("After shifting list is:", l)



# list = [4, 7, -2, 8, -11, 44, -7, -22]
#
#
# #
#
# list = [4, 7, -2, 8, -11, 44, -7, -22]
# list_len = len(list)
# j =0
# for i in range(list_len):
#     #print(i)
#     if list[i] <0:
#
#           temp = list[i]
#           list[i] = list[j]
#           list[j] =temp
#           j = j+1
#
#
# print("out",list)



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

# emp_id = input("Enter the employee ID to fetch details: ")
# for employee in employee_details:
#     if employee[0]== emp_id:
#       print(f" ID : {employee[0]},  Name:{employee[1]}, Emailid:{employee[2]}, City:{employee[3]}, Mob:{employee[4]}, Sal:{employee[5]}")
# else:
#         print("employee not found")
#
#update employee
# employee_updateid= input("enter employee id \n")
# employee_details_toupdate = ['emp_128', 'swapna', 'swapna@gmail.com','karna', 78975557987, 4000500 ]
# for employee in employee_details:
#     if employee[0]== employee_updateid:
#         employee[0:] = employee_details_toupdate[0:]
# print("updated info :", employee_details)

# delete employee

# deleted_employee = " "
# employee_delete = input("enter employee id to delete")
#
# for employee in employee_details:
#     if employee[0] == employee_delete:
#         deleted_employee = employee_details.remove(employee)
# print("deleted employe info", employee_details)

new_employee_details_add = ['emp_129', 'gorav', 'gorav@gmail.com', 'BLR', 677777, 800080]
employee_details.append(new_employee_details_add)
print("after adding the new employee", employee_details)
