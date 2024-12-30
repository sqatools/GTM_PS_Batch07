##################### add data to dictionar #################
dict_c = {'name' : 'Rahul', 'Age' : 25, 'Address' : 'Pune'}
dict_c['email'] = 'rahul@gmail.com'
print("result dict_c :", dict_c)
#result dict_c : {'name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'email': 'rahul@gmail.com'}




#####################################
#keys method() : this method return the list of keys in the given dictionary
# values method() : this method the values the list of values  in the  given dictionary

dict_d = {'name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'email': 'rahul@gmail.com'}

print("list of kays ", dict_d.keys())#list of kays  dict_keys(['name', 'Age', 'Address', 'email'])
print("list of values :", dict_d.values())#list of values : dict_values(['Rahul', 25, 'Pune', 'rahul@gmail.com'])




############################################################
#pop() method: this method remove the data of specific key from dictionary and return it.

dict_f = {'name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'email': 'rahul@gmail.com'}
val = dict_f.pop('Address')
print("remove value ", val)
print("dict_f :", dict_f)
#remove value  Pune
#dict_f : {'name': 'Rahul', 'Age': 25, 'email': 'rahul@gmail.com'}



###############################################

# popiteams() : this method remove key values pair and return it from dictionary.

dict_g = {'name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'email': 'rahul@gmail.com', 'phone': 9618191537}
data = dict_g.popitem()
print("removed data :", data)
print("dict_g :", dict_g)
#removed data : ('phone', 9618191537)
#dict_g : {'name': 'Rahul', 'Age': 25, 'Address': 'Pune', 'email': 'rahul@gmail.com'}



#########################################################
#clear method : this method clear all the data from dictionary, only blank dictionary will remain.
dict_j = {'Name' : 'Rahul', 'Age': 25, 'Address': 'chittoor', 'email': 'rahul@gmail.com', 'Phone': 9618191537}
dict_j.clear()
print("dict_j :", dict_j)
#dict_j : {}



#########################################
# we can complete dictionary variable from memory.

dict_k = {'Name' : 'Rahul', 'Age': 25, 'Address': 'chittoor', 'email': 'rahul@gmail.com', 'Phone': 9618191537}
del dict_k ['email']
print("dict_k :", dict_k)
print("dict_k :", dict_k)


#dict_k : {'Name': 'Rahul', 'Age': 25, 'Address': 'chittoor', 'Phone': 9618191537}
#dict_k : {'Name': 'Rahul', 'Age': 25, 'Address': 'chittoor', 'Phone': 9618191537}

####################################################
fruits_shop = {
    'fruits' : {'Apple': {'price': 200, 'stock': 500},
                'Mango': {'price': 150, 'stock' : 300},
                'Banana': {'price': 50, 'stock' : 400},
                'Lichhi' : {'price' : 250, 'stock' : 800}
                },
}
print(fruits_shop['fruit']['Banana']['price'])