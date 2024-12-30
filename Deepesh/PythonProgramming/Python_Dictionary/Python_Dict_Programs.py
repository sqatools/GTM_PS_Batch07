#  write a python program to create dictionary output
str1 = "Python Programming"
# get each character count without using count method
# output = {'P': 2, 'y': 1, 't': 1, 'o' : 2, .....}

output = {}
for char in str1:
    # print(output)
    if char not in output:
        output[char] = 1
    else:
        output[char] += 1

print(output)
# {'P': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}


# program2 :  write a python program to get average of all list values in given dictionary
dict2 = {'a': [3, 5, 7, 8],
         'b': [2, 6, 8, 9],
         'c': [1, 4, 7, 8]}

# 1. get sum of each list values
# output = {'a': 23, 'b': 25, 'c': 20}

# 2. get average of each list values
# output = {'a': 5.6, 'b': 6.2, 'c': 5}
output1 = {}
output2= {}

for key, value in dict2.items():
    output1[key] = sum(value)
    output2[key] = sum(value)/len(value)

print("sum of list data :", output1)
print("average of list data :", output2)
