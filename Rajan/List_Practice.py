my_list = [1, 2, 3, 4, 2, 5, 3, 6, 1]
unique_list = list(set(my_list))
print("list after removing duplicates:", unique_list)

print("-"*50)

my_list = [1, 2, 3, 4, 5]
reverse_list = []

for i in range(len(my_list) - 1, -1, -1):
    reverse_list.append(my_list[i])
print("Reversed list:", reverse_list)
