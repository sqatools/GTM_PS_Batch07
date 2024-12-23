# program : write a list program to remove all the duplicated from given list
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
