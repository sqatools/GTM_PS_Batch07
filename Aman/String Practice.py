# write a python program to find out all the mobile number and email from given string

str_B = """
str1 = " Hello python 8989898787 test@gail.com 5654645645 user2@tahoo.com Hope doing good"
"""

word_list = str_B.split(" ")
for word in word_list:
    if word.isnumeric() and len(word) == 10:
        print(word)
    else:
        continue
for word in word_list:
    if "@" in word:
        print(word)
    else:
        continue

print("_" * 50)
# Q: write a python to find out longest word in the given string

str_C = "Hello We Are Learning Python"
max_len = 0
longest_word = ''
word_list = str_C.split(" ")
print(max(word_list))

for word in word_list:  # I, have, been, Programming, using
    word_len = len(word)  # 1, 4, 4, 11, 5
    if word_len > max_len:  # 1> 0 | 4 > 1 | 4 > 4 | 11> 4 | 5> 11 | 6> 11
        max_len = word_len  # 1, 4, 11
        longest_word = word  # I, have, Programming
        print(longest_word)
    else:
        continue

print("logest word :", longest_word)
