my_list = [1, 2, 3, 4, 2, 5, 3, 6, 1]
unique_list = list(set(my_list))
print("list after removing duplicates:", unique_list)

print("-"*50)

my_list = [1, 2, 3, 4, 5]
reverse_list = []

for i in range(len(my_list) - 1, -1, -1):
    reverse_list.append(my_list[i])
print("Reversed list:", reverse_list)
print("_"*50)
cities = ["Chennai", "Bangalore", "Bambay", "Madurai", "Trichy", "Pune"]
val = [3, 4, 5, 6, 2, 9]
print(cities[0])
print(val[2])
print(cities[:3])
print(cities[-2])
print(cities[::2])
print(val)
cities[2] = "Bombay"
cities.insert(2,"london") # Insert
del cities  [4] # Remove using del
deleted = cities.pop() # Remove using Pop()
print(deleted + " has been deleted")
cities.append("-These are my favorite cities")
cities.sort()
print(cities)

print("_"*50)

list1 = [1, 2, 3, 4, 5, 4]
list2 = [6, 7, 8, 9]
list2.append(10) # Append
list1.extend(list2)
list1.remove(4)
print(list1)

print("-"*50)

