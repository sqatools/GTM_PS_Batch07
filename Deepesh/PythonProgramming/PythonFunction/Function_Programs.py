# 1. write a python program to get maximum from given list using function
list1 = [4, 6, 89, 22, 55, 44]
output = 89

def get_max_value(l1):
    max_val = 0
    for val in l1:
        if val > max_val:
            max_val = val
        else:
            continue

    return max_val

result = get_max_value(list1)
print("max value result :", result)

# 2. write a python function get count of each vowels from given string in dictionary.
str1 = "Hello Good Morning"
#output = {'e': 1, 'o': 4, 'i': 1}

def get_vowels_count(str_input):
    vowels = 'aeiou'
    output = {}
    for char in str_input:
        if char in vowels and char not in output:
            output[char] = str_input.count(char)
        else:
            continue

    return output


result2 = get_vowels_count(str1)
print("vowels count :", result2)
# vowels count : {'e': 1, 'o': 4, 'i': 1}
