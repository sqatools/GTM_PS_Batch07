# write a python program to find out all the mobile number and email from given string

str_A = """
str1 = " Hello python 8989898787 test@gail.com 5654645645 user2@tahoo.com Hope doing good"
"""

word_list = str_A.split(" ")
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
# Q: write a python to find out second longest word in the given string

str_B = "Hello We Are Learning Python"
max_len = 0
longest_word = ''
word_list = str_B.split(" ")
print(max(word_list))

for word in word_list:
    word_len = len(word)
    if word_len > max_len:
        max_len = word_len
        longest_word = word
        print(longest_word)
    else:
        continue

print("logest word :", longest_word)


str_p = "Hello We Are Learning Python"
output = "Python"
maxlen = 0
nextlen = 0
longword = ""
nextword = ""
wordlist = str_p.split(" ")

for word in wordlist:
    wordlen = len(word)
    if wordlen > maxlen:
        maxlen = wordlen
        longword = word
    elif maxlen > wordlen >nextlen:
        nextlen = wordlen
        nextword = word

print("Second longest word: ", nextword)

print(f"Total Bill Amount: {sum(price for _, price in [('tshirt', 300), ('lower', 400), ('Jeans', 1000), ('Jacket', 2000), ('Watch', 4000)])}")


