list1 = [34, 54, 67, 1, 87, 90]

def max_val(l1):
    max_value = 0
    for val in l1:
        if val > max_value:
            max_value = val
            # print(max_value)
        else:
            continue
    print(max_value)
max_val(list1)

print("-"*50)

list2 = [1, 2, 3, 4, 5]

def maximum_value(l1) :
    max_val1 = 0
    for val in list2:
        if val > max_val1:
            max_val1 = val
    print("value1 :", max_val1)

maximum_value(list2)


print("-"*50)

str1 = "hello we are learning python programming"


def ger_vowels_count(str_input):
    vowels = "aeiou"
    output = {}
    for char in str_input:
        if char in vowels:
            output[char] = str_input.count(char)
        else:
            continue
    print(output)

ger_vowels_count(str1)
# {'e': 4, 'o': 3, 'a': 3, 'i': 2}


def read_file(filepath):
    file = open(filepath, "r")
    data = file.read()
    print(data)
    file.close()

read_file("new_append_file.txt")

def write_content(filepath, content):
    file =  open(filepath, "w")
    data = file.write(content)
    print(data)
    file.close()

write_content("new_append_file", "hello i am working in tech mahindra. while i am currently assigned to buffer project, currently i don't have any work to do. thats why in this mean time i am learning python")

write_content("new_append_file","yes again i am trying to write something on this file. i will check")

def append_data(filepath, content):
    file = open(filepath, "a")
    data = file.write(content)
    print(data)
    file.close()

append_data("new_append_file", "\\lets see how it is going to work")

append_data("new_append_file", "\\lets see how it is going to work")
append_data("new_append_file", "\n lets see how it is going to work")

print("-"*50)

var_x = 100

def value1():
    var_y = 110
    print(var_x)
    print(var_y)


print("-"*50)
def value2():
    var_z = 120
    var_y = 200
    var_x = 250
    print(var_x)
    print(var_y)
    print(var_z)

print("-"*50)
def value3():
    global var_x
    var_a = 1
    var_x = 500
    print(var_a)
    print(var_x)

value1()
print("-"*50)
value2()
print("-"*50)
value3()
value1()


# give all the emails.

def get_all_mail(filepath):
    file_obj = open(filepath, 'r')
    data = file_obj.read()

    data_list = data.split(" ")
    output = []
    for word in data_list:
        if "@" in word:
            output.append(word)
        else:
            continue
    print(output)

get_all_mail("write_content_file.txt")


# Python function program to get unique values from the given list.
def unique_values(l1):
    list1 = list(l1)
    set1 = set(list1)
    unique_value1 = list(set1)
    print(unique_value1)

list2 = (1, 2, 3, 4, 5, 2, 6, 3, 7, 4, 8, 5, 9)
unique_values(list2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Python function program to get the duplicate characters from the string.
def duplicate_str(l2):
    output = []
    for char in l2:
        if l2.count(char) > 1:
            output.append(char)
    print(set(output))
str2 = "programming"
duplicate_str(str2)

def dup(l3):
    result = []
    for char in l3:
        if l3.count(char) > 1:
            result.append(char)
    print(set(result))
str5 = "hello we are "

dup(str5)
print("-"*50)
# 24). Python function program to get the square of all values in the given dictionary.
Input1 = {"a" : 4, "b" :3, "c" : 12, "d": 6}

def square(dict1):
    output= {}
    for k1, v1 in dict1.items():
        output[k1] = v1**2
    print(output)

square(Input1)

#25). Python function program to create dictionary output from the given string.
# Note: Combination of the first and last character from each word should be
# key and the same word will the value in the dictionary.
# Input2 = “Python is easy to Learn”
#Output = {‘Pn’: ‘Python’, ‘is’: ‘is’, ‘ey’: ‘easy’, ‘to’: ‘to’, ‘Ln’: ‘Learn’}

str4 = ("python is easy to learn")

def dict_output(l4):
    output = {}
    list_l4 = l4.split(" ")
    for word in list_l4:
        output[word[0]+word[-1]] = word
    print(output)

dict_output(str4)
# {'pn': 'python', 'is': 'is', 'ey': 'easy', 'to': 'to', 'ln': 'learn'}

# 26). Python function program to print a list of prime numbers from 1 to 100.
print("-"*50)
def prime_num(start, end):
    output = 0
    for val in range(start, end +1):
        if val >1:
            for num in range(2, int(val**0.5)+1):
                if val %num == 0:
                    break
                else:
                    output = val
    print(output)
prime_num(10, 15)



for num in range(2, 100):
    count = 1
    for val in range(2, (num//2+1)):
        if num%val == 0:
            count += 1
            break
        else:
            continue

    if count == 1:
        print(num, end=" ")


















