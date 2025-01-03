# set program practice

# program: write a python program to find the common values between two list
list1 = [4, 17, 9, 1, 5, 7]
list2 = ['a', 'b', 1, 5, 8, 4]

result = set(list1).intersection(set(list2))
print("common values :", list(result))
# common values : [1, 4, 5]

# solution2:
common_data = []
for val in list1:
    if val in list2:
        common_data.append(val)
    else:
        continue
        
print("common list data :", common_data)

