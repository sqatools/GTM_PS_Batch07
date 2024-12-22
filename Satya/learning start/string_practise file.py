str_a = "hello good morning"
result = ""
for char in str_a:
    if char not in result:
        result = result+ char
    else:
        continue
print(result)


print()
print("-"*50)

str_b = "satya santhi ram prasad satya loki santhi"

str_b_list = str_b.split(" ")

result = " "

for word in str_b_list:
    if word not in result:
        result = result + word+ " "
    else :
        continue
print(result)


print()

str_c = "hello i am learning python program"
max_len = 0
longest = ""
word_list = str_c.split(" ")

for word in word_list:
    word_len = len(word)
    if word_len > max_len:
        max_len = word_len
        longest = word
    else:
        continue
print(longest)

print()

# str_p = "Hello We Are Learning Python"
# max_len = 0
# longest_word = ""
# word_list = str_p.split(" ")
#
# for word in word_list: # Hello We Are Learning
#     word_len = len(word) # 5, 2 3, 8
#     if word_len > max_len: # 5 > 0 | 2 > 5 | 3 > 5 | 8 > 5
#         max_len = word_len # 5, 8
#         longest_word  = word # Hello, Learning
#     else:
#         continue

# print("Longest word :", longest_word) #

print("-"*50)
str_d = "satya chsatya@gmail.com user@yahoo.com 9490570891 8500631022 is good boy"

str_d_list = str_d.split(" ")

for word in str_d_list:
    if "@" in word:
        print(word)
    elif word.isnumeric() and len(word) == 10:
        print(word)
    else:
        continue
print("-"*50)
print()

str_e = "i am going to learning python programming"

str_e_list = str_e.split(" ")
largest = ""
second= ""
third = ""
for word in str_e_list:
    if len(word) > len(largest):
        third = second
        second = largest
        largest = word


    elif word != largest and len(word)>len(second):
        third = second
        second = word


    elif len(word)>len(third) and word != second and word != largest:
        third = word

# print(second) # python
print(third)


print("-"*50)
 # 1). Write a Python program to get a string made of the first and the last 2
# chars from a given string. If the string length is less than 2,
# return instead of the empty string


str_1 = "hello this is satya"
str_1_list = str_1.split()

for char in str_1_list:
    if len(char) == 2:
        print("true")
    elif len(char) > 2:
        print(char[:2]+char[-2:])


# 2). Python string program that takes a list of strings and returns
# the length of the longest string.

str2 = "hai i am in love with someone"
str2_list = str2.split()

max_len = 0
largest = ""

for word in str2_list:
    word_len = len(word)
    if word_len > max_len:
        max_len = word_len
        largest = word

    else:
        continue
print(largest)


print()
print("-"*50)

# 3). Python string program to get a string made of 4 copies of the last
# two characters of a specified string (length must be at least 2).

str3 = "hello"
result3 = str3[-2:]
result2 = result3*4
print(result2)


# 4). Python string program to reverse a string if it’s length is a multiple of 4.
print()
print("-"*50)
str4= "hell"

str_4_list = str4.split()

if len(str_4_list) % 4 == 0:
    print(str_4_list.reverse())
else:
    print("not divisible by 4")

# 5). Python string program to count occurrences of a substring in a string.

str_5 = "hello we are learning python"

print(str_5.count("l"))
print(str_5.count("e"))
print(str_5.count("o"))

# 6). Python string program to test whether a passed letter is a vowel or consonant.
print()
str_6 = "A"
vowles= ("A", "E", "I", "O" "U", "a", "e", "i", "o", "u")

if str_6 == "a" or "e" or "i" or "o" or "u" or "A" "E" "I" "O" "U":
    print("vowles :", str_6)
else:
    print("consonent")

# 7). Find the longest and smallest word in the input string.
print("-"*50)
str_7 = "hello we are learning python program"
str_7_list = str_7.split()

if str_7_list:
    max_len = max(str_7_list, key = len)
    min_len = min(str_7_list, key = len)
    print(max_len)
    print(min_len)

 # 8). Print most simultaneously repeated characters in the input string.













