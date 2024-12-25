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
__________________________________________________
#Total bill amount : 940
#[['Apple', 94, 20], ['Banana', 38, 10], ['Mango', 200, 75], ['Cherry', 150, 40], ['watermelon', 13, 100], ['PinaApple', 75, 150]]
