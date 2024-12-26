dict1 = {'a': 123, 'b' : 456, 'c': 789}
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

print("_"*50)
# Dict contains only unique keys, duplicate keys are not allowed.
# if we store the data with duplicate key, then latest defined data will considered.

dict2 = {'Name': 'Rahul', 'age': 23, 'email': 'rahul@gmail.com', 'phone': 4354435, 'age':45}
print(dict2)
# {'Name': 'Rahul', 'age': 45, 'email': 'rahul@gmail.com', 'phone': 4354435}


print("_"*50)
# Dict only allow immutable data type as key, int, float, string, tuple, boolean
dict3 = {2: 'Hello', 3.4: [4, 5, 6],
         'ABC' : (3, 5, 7), (1, 2, 3): {'a' : 123, 'b' : 456},
         True : 345, }
         # [4, 6, 7] : 3939}  # TypeError: unhashable type: 'list'

print(dict3)
# {2: 'Hello', 3.4: [4, 5, 6], 'ABC': (3, 5, 7), (1, 2, 3): {'a': 123, 'b': 456}, True: 345}


print("_"*50)
# Loop on dictionary data
dict_a = {'a': 111, 'b' : 222, 'c' : 444}
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

print("_"*50)
########### add data to the dictionary #############
#update method :
dict_b = {'a' : 3, 'b': 20, 'c': 500}

dict_c = {'P' : 111, 'Q': 567}

dict_b.update(dict_c)

print("output dict_b :", dict_b)
# {'a': 3, 'b': 20, 'c': 500, 'P': 111, 'Q': 567}

print("output dict_c :", dict_c)
# {'P': 111, 'Q': 567}


###### Get method ######
print(dict_b.get('P')) # 111

######## add data to dictionay ######

dict_b['Python'] = 'Programming'
print("result :", dict_b)
#  {'a': 3, 'b': 20, 'c': 500, 'P': 111, 'Q': 567, 'Python': 'Programming'}
