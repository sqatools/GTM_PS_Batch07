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
str1 = " Hello python 8989898787 test@gail.com 5654645645 user2@tahoo.com Hope doing good"

#5. write a python program to second largest word from given string.
str_p = "Hello We Are Learning Python"
output = "Python"


