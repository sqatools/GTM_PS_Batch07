list_A = [2, 4, 6, 88, 66, 45, 123]
print(list_A)

#program : write a python program provide the shopping bill amount from list of items purchased
list3 = [('tshirt', 300),
         ('lower', 400),
         ('Jeans', 1000),
         ('Jacket', 2000),
         ('Watch', 4000)]
# result provide the total bill amount
print("-"*50)
# second largest number
list_b = [4, 5, 6 ,77, 88, 55, 4444, 67, 4564]
max_len = 0
second_lar = 0
# largest = ("")

for val in list_b:
    if val> max_len:
        second_lar = max_len
        max_len = val
    if val<max_len and val> second_lar:
        second_lar = max_len

print(second_lar)
# 4444


# positive values in left side and negative values right side
list_c = [4, -119, 77, -23, 11, -7,  8, 9, -11, ]

positive = [num for num in list_c if num > 0]
negative = [num for num in list_c if num < 0]

result8 = positive + negative
print(result8)


#  Python program to calculate the square of each number from the given list.
print("-"*50)
list_4 = [2, 3, 4, 5, 6, 7]
for val in list_4:
    square_val = val**2
    print(square_val, end=" ")

# 2). Python program to combine two lists.
print()
list_e = [2, 3, 4, 5, 6, 7]
list_f = [8, 9, 10, 11]

result9 = list_e + list_f
print(result9)

 # 3). Python program to calculate the sum of all elements from a list.

list_g = [2, 3, 4, 5, 6, 7, 8 ,9]

result10 = sum(list_g)
print(result10)

# 4). Python program to find a product of all elements from a given list.

list_A = [2, 3, 4]
result = 10*list_A
print(result)
result2 = (list_A)*5
print(result2)
product = 1
for num in list_A:
    product *= num
print(product)























