#Q1 : write a python program to remove duplicate character
str1 = "We are Learning Python"
result = ""
for char in str1:
    if char not in result:
        result = result + char
    else:
        continue

print("Result :", result)
# Result : We arLnigPytho


print("_"*50)
# write a python program to remove duplicate words from given string.

str_x = "John Mohan Mohit Rahul Ravi Mohit Rahul John"
#output = "John Mohan Mohit Rahul Ravi"
world_list = str_x.split(" ")  # create word list with spaces.
print(world_list)

result = ""  # John Mohan Mohit Rahul Ravi

# apply loop on word_list
for word in world_list: #John Mohan Mohit Rahul Ravi
    # check word not in result, then add in the result
    if word not in result:
        result = result + word + " "
    else:
        continue

print("result data :", result)


print("_"*50)
#Q3 : Write a python program to get longest word from given string.
str_p = "Hello We Are Learning Python"
max_len = 0
longest_word = ""
word_list = str_p.split(" ")

for word in word_list: # Hello We Are Learning
    word_len = len(word) # 5, 2 3, 8
    if word_len > max_len: # 5 > 0 | 2 > 5 | 3 > 5 | 8 > 5
        max_len = word_len # 5, 8
        longest_word  = word # Hello, Learning
    else:
        continue

print("Longest word :", longest_word) # Learning


#4. Write a python program to get email and phone number from given string
str1 = "Hello python 8989898787 test@gail.com 5654645645 user2@tahoo.com Hope doing good"

#5. write a python program to second largest word from given string.
str_p = "Hello We Are Learning Python"
output = "Python"

print()
# solution: Write a python program to get email and phone number from given string
str_a = "Hello python 8989898787 test@gmail.com 5654645645 user2@yahoo.com Hope 345 doing good"

word_list = str_a.split(" ")
for word in word_list:
    if "@" in word:
        print(word)
    elif word.isnumeric() and len(word) == 10:
        print(word)
    else:
        continue



print("_"*50)
#5. write a python program to find second largest word from given string.
str_p = "Hello LearninR Qrogramming Learning We Are Programming Python"
# output = "Python"

largest_word = ""
sec_large = ""
word_list = str_p.split(" ")
print(word_list)
# ['Hello', 'We', 'Are', 'Learning', 'Python']

for word in word_list:
    #print(word)
    if len(word) > len(largest_word): # 5 > 0 | 2 > 5 | 3> 5 | 8> 5 | 6 > 8
        sec_large = largest_word
        largest_word = word # Hello, Learning

    if len(word) < len(largest_word) and len(word) > len(sec_large):
        # 2 < 5 and 2 > 0
        # 3 < 5 and 3 > 2
        # 6 < 8 and 6 > 3
        sec_large = word # We, Are, Python

print("second large word :", sec_large)





