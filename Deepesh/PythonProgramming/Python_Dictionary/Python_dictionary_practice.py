dict1 = {'a': 123, 'b': 456, 'c': 789}
print(dict1, type(dict1))
"""
# properties
-> Dictionary is mutable data type we can modify at point of time.
-> Dict store data in key value pair.
-> Dict contains only unique keys, duplicate keys are not allowed.
-> Dictionary does not follow the indexing, its LIFO(Last In First Out) concept.
-> Dict only allow immutable data type as key, int, float, string, tuple, boolean.
-> Dict allow type of data as value, int, float, string, dictionary, set, boolean.
"""

# Dictionary is mutable data type we can modify at point of time.
dict1['d'] = 888
print("dict1 :", dict1)

print("_" * 50)
# Dict contains only unique keys, duplicate keys are not allowed.
# if we store the data with duplicate key, then latest defined data will considered.

dict2 = {'Name': 'Rahul', 'age': 23, 'email': 'rahul@gmail.com', 'phone': 4354435, 'age': 45}
print(dict2)
# {'Name': 'Rahul', 'age': 45, 'email': 'rahul@gmail.com', 'phone': 4354435}


print("_" * 50)
# Dict only allow immutable data type as key, int, float, string, tuple, boolean
dict3 = {2: 'Hello', 3.4: [4, 5, 6],
         'ABC': (3, 5, 7), (1, 2, 3): {'a': 123, 'b': 456},
         True: 345, }
# [4, 6, 7] : 3939}  # TypeError: unhashable type: 'list'

print(dict3)
# {2: 'Hello', 3.4: [4, 5, 6], 'ABC': (3, 5, 7), (1, 2, 3): {'a': 123, 'b': 456}, True: 345}


print("_" * 50)
# Loop on dictionary data
dict_a = {'a': 111, 'b': 222, 'c': 444}
print(dict_a)

for val in dict_a.items():
    print(val)
"""
('a', 111)
('b', 222)
('c', 444)

"""
for k1, v1 in dict_a.items():
    print('Key :', k1)
    print('value :', v1)

# dictionary methods
#########################################
print(dir(dict))
"""
'clear', 'copy', 'fromkeys', 'get', 'items', 
'keys', 'pop', 'popitem', 'setdefault', 
'update', 'values']
"""

print("_" * 50)
########### add data to the dictionary #############
# update method : This method update data from one dictionary to another.

dict_b = {'a': 3, 'b': 20, 'c': 500}

dict_c = {'P': 111, 'Q': 567}

dict_b.update(dict_c)

print("output dict_b :", dict_b)
# {'a': 3, 'b': 20, 'c': 500, 'P': 111, 'Q': 567}

print("output dict_c :", dict_c)
# {'P': 111, 'Q': 567}


###### Get method ######
# get() method :  Get method return the value of specific key.

print(dict_b.get('P'))  # 111

print("_" * 50)
######## add data to dictionary ######

dict_c = {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune'}

dict_c['email'] = 'rahul@gmail.com'
print("result dict_c :", dict_c)
# {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'email': 'rahul@gmail.com'}


print("_" * 50)
####################
# keys method() :  This method return  the list of keys in the given dictionary
# values method() :  This method return the list of values in the given dictionary.

dict_d = {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'email': 'rahul@gmail.com'}

print("list of keys :", dict_d.keys())
# dict_keys(['Name', 'Age', 'Address', 'email'])

print("List of values :", dict_d.values())
# dict_values(['Rahul', 25, 'Pune', 'rahul@gmail.com'])


print("_" * 50)
####################
# items() method : This method return the tuple of key value pair in list
dict_e = {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'email': 'rahul@gmail.com'}
print("Items  :", dict_e.items())
# [('Name', 'Rahul'), ('Age', 25), ('Address', 'Pune'), ('email', 'rahul@gmail.com')]


print("_" * 50)
####################
# pop() method: This method remove the data of specific key from dictionary and return it.
dict_f = {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'email': 'rahul@gmail.com', '': 656456,
          'phone': None}
val = dict_f.pop('Address')
print("removed value :", val)
# dict_f : {'Name': 'Rahul', 'Age': 25, 'email': 'rahul@gmail.com', '': 656456, 'phone': None}


print("_" * 50)
####################
# popitems() :  This method remove key value pair and return it from dictionary.

dict_g = {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'email': 'rahul@gmail.com', 'Phone': 656456}
data = dict_g.popitem()
print("removed data :", data)  # ('Phone', 656456)
print("dict_g :", dict_g)
# {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'email': 'rahul@gmail.com'}


print("_" * 50)
#####################
# clear method : This method clear all the data from dictionary, only blank dictionary will remain.
dict_j = {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'email': 'rahul@gmail.com', 'Phone': 656456}
dict_j.clear()
print("dict_j :", dict_j)  # {}

print("_" * 50)
#####################
# del function : ->  We can delete specific key value combination from given dictionary
#                ->  We can delete complete dictionary variable from memory.

dict_k = {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'email': 'rahul@gmail.com', 'Phone': 656456}
del dict_k['email']
print("dict_k :", dict_k)
# {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'Phone': 656456}

# delete dictionary variable from memory
del dict_k
# print("dict_k :", dict_k)
# NameError: name 'dict_k' is not defined.


print("_" * 50)
#####################
# copy method :  This method copy content from one list to another.
# There are two type of copy
# 1). Shallow Copy   2). Deep copy

# Shallow copy
dict_x = {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'Phone': 656456}
dict_y = dict_x
dict_y['email'] = 'testuser1@gmail.com'
print("dict_x :", dict_x)
print("dict_y :", dict_y)
# Both dictionary will have same data.


# Deep Copy : In this copy method, we have to .copy explicitly to copy content from one dictionary to
#             another dictionary, and if we will changes in any of the dictionary, then it will not
#             reflect on another dictionary.

dict_p = {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'Phone': 656456}
dict_q = dict_p.copy()
dict_q['salary'] = 200000

print("dict_p :", dict_p)
# {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'Phone': 656456}
print("dict_q :", dict_q)
# {'Name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'Phone': 656456, 'salary': 200000}


print("_" * 50)
#####################
# setdefault method(): -> setdefault method set a default value to new key and add in dictinary
#                       -> set default method return the value of existing key and does not change
#                          anything.

dict_w = {'P': 123, 'Q': 456, 'R': 333, 'S': 343}
val = dict_w.setdefault('T', 500)
print("dictionary value: ", val)
print("dict_w :", dict_w)

val2 = dict_w.setdefault('R', 1000)
print("dictionary value: ", val2)
print("dict_w :", dict_w)

dict_w['R'] = 2000
print("dict_w :", dict_w)

print("_" * 50)
#####################
# fromkeys method: This method assign one value to the list of keys.

list1 = ['a', 'b', 'c', 'd', 'e']
result = dict.fromkeys(list1, 50)
print("result :", result)
# {'a': 50, 'b': 50, 'c': 50, 'd': 50, 'e': 50}

##########################################
# create a dictionary with zip function
list_A = ['a', 'b', 'c', 'd', 'e']
list_B = [10, 20, 30, 40, 50]

result = dict(zip(list_A, list_B))
print("RESULT :", result)
# {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}


print("_" * 50)
############################################
# deal with complex dictionary data

fruits_shop = {
    'fruits': {'Apple': {'price': 200, 'stock': 500},
               'Mango': {'price': 150, 'stock': 300},
               'Banana': {'price': 50, 'stock': 400},
               'Lichhi': {'price': 250, 'stock': 800}
               },
}

print(fruits_shop['fruits']['Banana']['price'])  # 50


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



