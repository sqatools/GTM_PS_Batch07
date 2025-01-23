# 1.  Python Program to add two integer values.
'''
a = 15
b = 12

print(a+b)

# 2. Python Program to subtract two integer values.

print(a-b)

# 3). Python program to multiply two numbers.

print(a*b)

# 4). Python program to repeat a given string 5 times.

# Input :
str1 = "SQATools"
print(str1*5)

# 5).Python program to get the Average of given numbers.
c=11
print((a+b+c)/3)
'''
print ("_"*50)
'''
# 1). Python program to check given number is divided by 3 or not.

x = input("Enter the input value:")
x = int(x)
if x%3 == 0 :
    print(" This value is divisible by 3")
else :
    print("This value is not divisible by 3")
'''

# 4). Python program to check the given number divided by 3 and 5.
'''
x = input ("Enter the input value:")
x = int(x)
if x%3 == 0 and x%5 == 0:
    print ("The number is divided by 3 and 5")
else:
    print ("The number is not divided by 3 and 5")

'''
'''
# 5). Python program to print the square of the number if it is divided by 11.
x = input ("Enter the input value:")
x = int(x)
if x%11 == 0:
    print("The square of the number is: ", x**2)
else :
    print ("The number is not divisible by 11")
'''
# 7). Python program to check given number is odd or even.
'''
x = input ("Enter the input value:")
x = int(x)
if x%2 == 0:
    print ("The given number is an even number")
else :
    print ("The given number is an odd number")
'''
# 9). Python program to check authentication with the given username and password.
'''
a = input("Enter the username: ")
b = input("Enter the password: ")

if a == "username" and b == "password":
    print("Welcome")
else:
    print("Your credentials are wrong")
'''
# 10). Python program to validate user_id in the list of user_ids.
'''
user_ids = [123,456,789,234,567,891]
x = input("Enter the user id: ")
x=int(x)
if x in user_ids :
    print("user id is correct")
else:
    print("user id is invalid")
'''

#11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
'''
x = input("Enter the value: ")
x = int(x)
if x%2 == 0:
    print("The square of the value is:", x**2)
elif x%3 == 0:
    print("The cube of the value is: ",x**3)
else:
    print("The number is not divisible by 2 or 3")
'''
'''
#14). Python program to find the largest number among three numbers.

x = int(input("Enter the first number:"))
y = int(input("Enter the Second number:"))
z = int(input("Enter the Third number:"))

if x>=y and x>=z :
    print ("The greatest number is", x)
elif y>=x and y>=z:
    print ("The greatest number is: ", y)
else:
    print ("The greatest number is", z)

'''
'''
# 15). Python program to check any person eligible to vote or not

x = int(input("Enter your age:"))

if x>= 18 :
    print("You are eligible to vote")
else:
    print("You are not eligible for vote")
'''
# 16). Python program to check whether any given input is a palindrome.
'''
x = input("Enter the input:")

y = x[::-1]

if x == y :
    print ("The given input is a palindrome")
else :
    print("The given input is not a palindrome")
'''
# 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
'''
x = int(input("Enter the mark:"))

if x>= 35:
    print("PASS")
else :
    print("FAIL")
'''
# 19). Python program to check whether the given number is positive or negative.
'''
x = int(input("Enter the number:"))

if x >= 0:
    print("The number is positive")
else :
    print("The number is negative")
'''
# 21). Python program to check whether the given number is positive or negative and even or odd.
'''
x = int(input("Enter the number:"))

if x>=0:
    if x%2 == 0:
        print("The given number is positive and even")
    else:
        print("The given number is positive and odd")
else :
    if x%2 == 0:
        print("The given number is negative and even")
    else:
        print("The given number is negative and odd")
'''
# 22). Python program to print the largest number from two numbers.
'''
x = int(input("Enter the first number:"))
y = int(input("Enter the Second number:"))

if x>=y:
    print("The largest number is: ", x)
else:
    print("The largest number is: ", y)
'''
# 32). Python program to check whether an alphabet is a vowel.
'''
vowel = ['A','E','I','O','U','a','e','i','o','u']
x=input("Enter the character: ")

if x in vowel :
    print("The given character is a vowel")
else :
    print("The given character is not a vowel")
'''

# 34).  Python program to convert the month name to the number of days.
'''
x=input("Enter the Month: ")

if x == ("january" or "march" or "may" or "july" or "august" or "october" or "december") :
    print ("Number of days is 31")
elif x == ("april" or "june" or "september" or "november"):
    print("Number of days is 30")
elif x == ("february"):
    print("Number of days is 28 or 29")
else:
    print("Invalid Month")
'''

# 52). A shop will give a 10% discount if the bill is more than 1000, and 20% if the bill is more than 2000. Using the python program Calculate the discount based on the bill.
'''
x = int(input("Enter the total bill amount: "))

if 2000 >= x > 1000 :
    print ("The discount is 10%")
elif x> 2000:
    print ("The discount is 20%")
else:
    print("No discount")
'''
'''
for x in range(1, 101):
    print(x)

for y in range(1,21):
    if y%2!=0 :
        print(y)
'''
# 1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
'''
for i in range(1500,2701):
    if i%5 == 0 and i%7 == 0:
        print(i,end=" ")
'''
# 4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
'''
Input = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even = 0
odd = 0

for i in Input:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd)
'''
# 5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
'''
for i in range(0,7):
    if i!=3 and i!=6:
        print(i)
'''
#6). Write a program to get the Fibonacci series between 0 to 20 using python.
'''
x=0
y=1
for i in range(0,21):
    print(x, end=" ")
    z = x+y
    x=y
    y=z
    
'''
'''
29). Python program to find the electricity bill. According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 250 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill

units = int(input("Enter the total units: "))
Amount = 0

for i in range(0,units+1):
    if i <= 50:
        Amount = Amount + 0.5
    elif 100 >= i >50:
        Amount = Amount + 0.75
    elif 250 >= i> 100:
        Amount = Amount + 1.25
    elif i >250:
        Amount = Amount + 1.5

Total_Amount = Amount + (Amount*0.17)
print("The final bill is ", Total_Amount)
'''
# 16). Python Loops program to find the sum of all natural numbers between 1 to n using python.
# sum of all even and odd numbers between 1 to n using python.
'''
n = int(input("Enter the number: "))
sum = 0
even = 0
odd = 0

for i in range(1,n+1):
    sum+=i


for j in range(1,n+1):
    if j%2 == 0:
        even+=j
    else:
        odd+=j
print("Sum of even values: ",even)
print("Sum of odd values: ",odd)
print("Sum of all values: ",sum)
'''
'''
num = int(input("Enter a number: "))
count = 1

for i in range(2, num):
    if num%i == 0:
        count += 1

print(count)
if count > 1:
    print("It is not prime number")
else:
    print("It is a prime number")
'''
'''
str1 = "Virat is best India player"

print(str1[1:-1])

w1=str1[0:5]
w2=str1[6:9]
w3=str1[9:13]
w4=str1[14:19]
w5=str1[20:]
print(w1[0]+w1+" "+w2[0]+w2+" "+w3[0]+w3+" "+w4[0]+w4+" "+w5[0]+w5)
'''
'''
# str1 = We are learning Python Programming
# 1. swap first and last character of each word
# 2. Reverse each word of a string

str1 = "We are learning Python Programming"
w1=str1[0:2]
w2=str1[3:6]
w3=str1[7:15]
w4=str1[16:22]
w5=str1[23:]
print(f"{w1[::-1]} {w2[::-1]} {w3[-1]}{w3[1:-1]}{w3[0]} {w4[-1]}{w4[1:-1]}{w4[0]} {w5[-1]}{w5[1:-1]}{w5[0]}")
print(f'{w1[::-1]} {w2[::-1]} {w3[::-1]} {w4[::-1]} {w5[::-1]}')
'''
'''
#4. Write a python program to get email and phone number from given string
str1 = "Hello python 8989898787 test@gail.com 5654645645 user2@tahoo.com Hope doing good"

wordlist = str1.split(" ")
at = "@"
phone = ""
email = ""
#print(wordlist)
for word in wordlist:
    if word.isnumeric() and len(word) == 10:
        phone = phone + word + " "
    elif at in word:
        email = email + word + " "



print("Phone numbers: ", phone)
print("email id: ", email)



#5. write a python program to second largest word from given string.
str_p = "Hello We Are Learning Python"
output = "Python"
maxlen = 0
nextlen = 0
longword = ""
nextword = ""
wordlist = str_p.split(" ")

for word in wordlist:
    wordlen = len(word)
    if wordlen > maxlen:
        maxlen = wordlen
        longword = word
    elif maxlen > wordlen >nextlen:
        nextlen = wordlen
        nextword = word

print("Second longest word: ", nextword)

#program : write a python program provide the shopping bill amount from list of items purchased
list3 = [('tshirt', 300),
         ('lower', 400),
         ('Jeans', 1000),
         ('Jacket', 2000),
         ('Watch', 4000)]
# result provide the total bill amount

result = 0

for i in list3:
    result = result + i[-1]

print("Total Bill Amount:", result)
'''
'''
# HW1 :  write a python program to second last max value from given list
list1 = [4, 6, 22, 77, 23, 44, 66, 100]
output = 77
max = 0
next=0
for i in list1:
    if i > max:
        next=max
        max=i
    elif max > i > next:
        next = i
print("second max value: ",next)


# HW2 :  write a python program to move all positive value in left side of the list
# and negative to right side of the list
list2 = [4, 7, -2, 8, -11, 44, -7, -22]
# output = [4, 7, 8, 44, -2, -11, -7, -22]
list2a = []
list2b = []

for i in list2:
    if i > 0:
        list2a.append(i)
    else:
        list2b.append(i)

Result = list2a + list2b
print("output =", Result)

# HW : Write a Python Program to create a employee management system with the help of list structure.

employee_details = [
    ['emp_123', 'rahul', 'rahul@gmail.com', 'Pune', 7897897987, 400000],
    ['emp_124', 'mohit', 'mohit@gmail.com', 'Pune', 5435345343, 500000],
    ['emp_125', 'pooja', 'pooja@gmail.com', 'Pune', 5435345432, 600000],
    ['emp_126', 'gourav', 'gourav@gmail.com', 'Pune', 4434543223, 700000],
    ['emp_127', 'sourav', 'sourav@gmail.com', 'Pune', 7897888886, 800000],
]
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
'''
'''
#2). Python Dictionary program to print the square of all values in a dictionary.
Input = {'a': 5,'b' : 3, 'c' :6, 'd' : 8 }


for k1,v1 in Input.items():
    print(k1 ,":", v1**2)


#3). Python Dictionary program to move items from dict1 to dict2.
dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
dict2 = {}

for k1,v1 in dict1.items():
    dict2[k1] = v1
dict1.clear()
print("dict1 :", dict1)
print("dict2 :", dict2)
'''
'''
dict2 = {'a': [3, 5, 7, 8],
         'b': [2, 6, 8, 9],
         'c': [1, 4, 7, 8]}


#1. get sum of each list values
dict3 = {}
for k1,v1 in dict2.items():
    dict3[k1] = sum(v1)
print(dict3)
#2. get average of each list values
dict4 = {}
for k1,v1 in dict2.items():
    dict4[k1] = sum(v1)/len(v1)
print(dict4)
'''

it_company = {
    'HR': {
        'Recruiter HR': [
            {'name': 'Aarav Sharma', 'email': 'aarav.sharma@itcompany.com', 'phone': '987-654-3210'},
            {'name': 'Ishita Verma', 'email': 'ishita.verma@itcompany.com', 'phone': '987-654-3211'}
        ],
        'Activity HR': [
            {'name': 'Ananya Reddy', 'email': 'ananya.reddy@itcompany.com', 'phone': '987-654-3212'},
            {'name': 'Karan Singh', 'email': 'karan.singh@itcompany.com', 'phone': '987-654-3213'}
        ],
        'Payroll HR': [
            {'name': 'Priya Patel', 'email': 'priya.patel@itcompany.com', 'phone': '987-654-3214'},
            {'name': 'Vikram Joshi', 'email': 'vikram.joshi@itcompany.com', 'phone': '987-654-3215'}
        ]
    },
    'Management': {
        'Managers': [
            {'name': 'Sanya Gupta', 'email': 'sanya.gupta@itcompany.com', 'phone': '987-654-3216'},
            {'name': 'Rohit Mehta', 'email': 'rohit.mehta@itcompany.com', 'phone': '987-654-3217'},
            {'name': 'Meera Chawla', 'email': 'meera.chawla@itcompany.com', 'phone': '987-654-3218'}
        ],
        'Teamlead': [
            {'name': 'Kabir Kapoor', 'email': 'kabir.kapoor@itcompany.com', 'phone': '987-654-3219'},
            {'name': 'Simran Bhatia', 'email': 'simran.bhatia@itcompany.com', 'phone': '987-654-3220'},
            {'name': 'Aditya Sethi', 'email': 'aditya.sethi@itcompany.com', 'phone': '987-654-3221'}
        ],
        'Module Lead': [
            {'name': 'Riya Nair', 'email': 'riya.nair@itcompany.com', 'phone': '987-654-3222'},
            {'name': 'Neeraj Malhotra', 'email': 'neeraj.malhotra@itcompany.com', 'phone': '987-654-3223'},
            {'name': 'Divya Yadav', 'email': 'divya.yadav@itcompany.com', 'phone': '987-654-3224'}
        ]
    },
    'Development': {
        'UI Dev': {
            'Sr Dev': [
                {'name': 'Rahul Rao', 'email': 'rahul.rao@itcompany.com', 'phone': '987-654-3225'},
                {'name': 'Neha Mishra', 'email': 'neha.mishra@itcompany.com', 'phone': '987-654-3226'}
            ],
            'Jr Dev': [
                {'name': 'Tara Kulkarni', 'email': 'tara.kulkarni@itcompany.com', 'phone': '987-654-3227'},
                {'name': 'Amit Deshmukh', 'email': 'amit.deshmukh@itcompany.com', 'phone': '987-654-3228'}
            ]
        },
        'API Dev': {
            'Sr Dev': [
                {'name': 'Rajesh Menon', 'email': 'rajesh.menon@itcompany.com', 'phone': '987-654-3229'},
                {'name': 'Pooja Ghosh', 'email': 'pooja.ghosh@itcompany.com', 'phone': '987-654-3230'}
            ],
            'Jr Dev': [
                {'name': 'Manoj Choudhury', 'email': 'manoj.choudhury@itcompany.com', 'phone': '987-654-3231'},
                {'name': 'Lavanya Shetty', 'email': 'lavanya.shetty@itcompany.com', 'phone': '987-654-3232'}
            ]
        },
        'Database Dev': {
            'Sr Dev': [
                {'name': 'Anil Gupta', 'email': 'anil.gupta@itcompany.com', 'phone': '987-654-3233'},
                {'name': 'Shalini Iyer', 'email': 'shalini.iyer@itcompany.com', 'phone': '987-654-3234'}
            ],
            'Jr Dev': [
                {'name': 'Gautam Kulkarni', 'email': 'gautam.kulkarni@itcompany.com', 'phone': '987-654-3235'},
                {'name': 'Sanya Bajaj', 'email': 'sanya.bajaj@itcompany.com', 'phone': '987-654-3236'}
            ]
        }
    },
    'Support': {
        'Internal Support': [
            {'name': 'Devika Singh', 'email': 'devika.singh@itcompany.com', 'phone': '987-654-3237'},
            {'name': 'Ajay Pawar', 'email': 'ajay.pawar@itcompany.com', 'phone': '987-654-3238'}
        ],
        'Customer Support': [
            {'name': 'Ritu Jain', 'email': 'ritu.jain@itcompany.com', 'phone': '987-654-3239'},
            {'name': 'Naveen Khan', 'email': 'naveen.khan@itcompany.com', 'phone': '987-654-3240'}
        ]
    },
    'Testing': {
        'Manual Tester': [
            {'name': 'Radhika Basu', 'email': 'radhika.basu@itcompany.com', 'phone': '987-654-3241'},
            {'name': 'Suresh Patil', 'email': 'suresh.patil@itcompany.com', 'phone': '987-654-3242'}
        ],
        'Automation Tester': [
            {'name': 'Mitali Joshi', 'email': 'mitali.joshi@itcompany.com', 'phone': '987-654-3243'},
            {'name': 'Vishal Prasad', 'email': 'vishal.prasad@itcompany.com', 'phone': '987-654-3244'}
        ],
        'Performance Tester': [
            {'name': 'Shruti Kulkarni', 'email': 'shruti.kulkarni@itcompany.com', 'phone': '987-654-3245'},
            {'name': 'Akash Desai', 'email': 'akash.desai@itcompany.com', 'phone': '987-654-3246'}
        ],
        'Security Tester': [
            {'name': 'Tanvi Kapoor', 'email': 'tanvi.kapoor@itcompany.com', 'phone': '987-654-3247'},
            {'name': 'Rakesh Rao', 'email': 'rakesh.rao@itcompany.com', 'phone': '987-654-3248'}
        ]
    },
    'Administration': {
        'Payroll admin': [
            {'name': 'Parul Nair', 'email': 'parul.nair@itcompany.com', 'phone': '987-654-3249'},
            {'name': 'Sameer Ahuja', 'email': 'sameer.ahuja@itcompany.com', 'phone': '987-654-3250'}
        ],
        'Employee admin': [
            {'name': 'Sneha Reddy', 'email': 'sneha.reddy@itcompany.com', 'phone': '987-654-3251'},
            {'name': 'Ravi Sharma', 'email': 'ravi.sharma@itcompany.com', 'phone': '987-654-3252'}
        ],
        'Facility admin': [
            {'name': 'Meghna Dixit', 'email': 'meghna.dixit@itcompany.com', 'phone': '987-654-3253'},
            {'name': 'Vijay Goel', 'email': 'vijay.goel@itcompany.com', 'phone': '987-654-3254'}
        ]
    }
}
print("_"*50)
'''
from pprint import pprint
pprint(it_company['HR']['Payroll HR'][1]['phone']) # 987-654-3215

# get all the employee details
# get specific employee details with their name

# # get all the employee details
for k1, v1 in it_company.items():
    #print(k1, ":", v1)
    for k2, v2 in v1.items():
        #print(k2,":", v2)
        if isinstance(v2, list):
            for data in v2:
                print(data)
        elif isinstance(v2, dict):
            for k3, v3 in v2.items():
                #print(k3, ":", v3)
                for data in v3:
                    print(data)



print("_"*50)

# get specific employee details with their name
emp_name = 'Sameer Ahuja'
mobile_no = ''

for k1, v1 in it_company.items():
    #print(k1, ":", v1)
    for k2, v2 in v1.items():
        #print(k2,":", v2)
        if isinstance(v2, list):
            for data in v2:
                #print(data)
                if data['name'] == emp_name or data['phone'] == mobile_no:
                    #print(data)
                    print(f"Name: {data['name']}\nEmail: {data['email']} \nPhone: {data['phone']}")

        elif isinstance(v2, dict):
            for k3, v3 in v2.items():
                #print(k3, ":", v3)
                for data in v3:
                    #print(data)
                    if data['name'] == emp_name or data['phone'] == mobile_no:
                        #print(data)
                        print(f" Name: {data['name']}\nEmail: {data['email']} \nPhone: {data['phone']}")
'''
print("_"*50)
# HW :
# Update Employee Details
'''
x = input("Enter the employee details for update: ")
y = input("Enter the detail you want to update:  ")
update = input("Enter the updated detail: ")


for k1, v1 in it_company.items():
    #print(k1, ":", v1)
    for k2, v2 in v1.items():
        #print(k2,":", v2)
        if isinstance(v2, list):
            for data in v2:
                #print(data)
                if data['name'] == x or data['phone'] == x or data['email'] == x:
                    data[y] = update
                    #print(data)
                    print(f"Name: {data['name']}\nEmail: {data['email']} \nPhone: {data['phone']}")

        elif isinstance(v2, dict):
            for k3, v3 in v2.items():
                #print(k3, ":", v3)
                for data in v3:
                    #print(data)
                    if data['name'] == x or data['phone'] == x or data['email'] == x:
                        data[y] = update
                        #print(data)
                        print(f"Name: {data['name']}\nEmail: {data['email']} \nPhone: {data['phone']}")
'''
# Delete Employee Details
'''
x = input("Enter the employee details to delete: ")
for k1, v1 in it_company.items():
    #print(k1, ":", v1)
    for k2, v2 in v1.items():
        #print(k2,":", v2)
        if isinstance(v2, list):
            for data in v2:
                #print(data)
                if data['name'] == x or data['phone'] == x or data['email'] == x:
                    v2.remove(data)

                    #print(data)
                    #print(f"Name: {data['name']}\nEmail: {data['email']} \nPhone: {data['phone']}")

        elif isinstance(v2, dict):
            for k3, v3 in v2.items():
                #print(k3, ":", v3)
                for data in v3:
                    #print(data)
                    if data['name'] == x or data['phone'] == x or data['email'] == x:
                        v3.remove(data)
                        #print(data)
                        #print(f"Name: {data['name']}\nEmail: {data['email']} \nPhone: {data['phone']}")
from pprint import pprint
pprint(it_company)
'''
# Add New employee Details
'''
x = input("Enter the employee department: ")
y = input("Enter the employee Role: ")
z = input("Enter the employee sub-role if he is in development: ")
Name = input("Enter the employee Name: ")
email = input("Enter the employee email id: ")
phone = input("Enter the employee phone number: ")
list1 = ['name', 'email', 'phone']
list2 = [Name, email, phone]
empdetails = dict(zip(list1, list2))
print(empdetails)
for k1, v1 in it_company.items():
    if k1 == x:
        for k2, v2 in v1.items():
            if k2 == y and isinstance(v2, list):
                v2.append(empdetails)
            elif k2 == y:
                for k3, v3 in v2.items():
                    if k3 == z:
                        v3.append(empdetails)
from pprint import pprint
pprint(it_company)
'''
'''
def find_email(file1):
    with open(file1,"r") as file1obj:
        file1data = file1obj.read()
       # print(file1data)
        worklist = file1data.split()
        for i in worklist:
            if "@" in i:
                print(i)

find_email("userdata.txt")
'''

def write(file,file1):
    with open(file,"r") as file:
        filedata = file.read()
        print(filedata)

   # with open(file1, "a") as file1obj:
       # file1data = file1obj.write(filedata)
        #print(file1data)

write("userdata.txt", "file1.txt")