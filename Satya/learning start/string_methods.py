##### string methods #####

str1 = "good morning"

print(str1[5]) # m
print(str1[-5]) # r
print(str1[:3]) # goo

####### string formatting #####

name = "satya"
age = "27"
city = "vbl"

# hell my name is satya and i am 27 years old and i am from vbl

print("hell my name is " +name+ " and i am "+age+ " years old and i am from " +city)
# result1 = "hell my name is {} and i am  {} years old and i am from {}".format(name, age, city))
# print(result1)

result2 = f"hell my name is {name} and i am {age} years old and i am from {city}"
print(result2)

result3 = f"i am {name} and i have 3 childerns at the age of {age} now i am leaving in {city}"
print(result3)

print(f"{name} +{age} +{city}")


print()
print("*"*50)
ask = r"hello \t this is satya \n i am \t software engineer\n\n in techm with \t 8lpa"
print(ask)



###### with indexing #######
print()
print("-"*50)
str2 = "i am learning python programming"

str2_lent = len(str2)
print(str2_lent) # 32

for i in range(str2_lent):
    print(i,str2[i])

####### ascii format######

# capital letter 65 to 90
# small letter 97 to 122
# ord for number
# chr for letter


print(ord('a')) # 97
print(ord('A')) # 65
print(ord('c')) # 99
print(ord('Z'))# 90

for i in range(65, 90):
    print(i, chr(i))



##### string slicing #######
print()
print("-"*50)

str3 = "hai this is satya"
print(str3[0:5]) # hai t

print(str3[::-1]) # aytas si siht iah

print(str3[-1:-11:-1]) # aytas si s

print(str3[2:-11]) # i th

str5 = "vvirat is best india playerr"
v= "v"
t = "t"
i = "i"
s= "s"
b = "b"
a = "a"
p = "p"
r = "r"
# print(str5[1:-1])
#
# result4 = f"{v}virat{t} {i}is{s} {b}best{t} {i}india{a} {p}player{r}"
# print(result4)
#
#
# v = "virat"
# i = "is"
# b= "best"
# p = "player"
#
# result6 = f"v{v}t i{i}s b{b}t p{p}r"
# print(result6)
#
#
# str = "i am a good boy"
#
# w1 = str[0:1]
# w2 = str[2:3]
# w3 = str[4:5]
# w4 = str[6:10]
# w5 = str[11:14]
#
# W2 = f"{w2[0]}{w2}{w2[-1]}"
# W3 = f"{w3[0]}{w3}{w3[-1]}"
# W4 = f"{w4[0]}{w4}{w4[-1]}"
# W5 = f"{w5[0]}{w5}{w5[-1]}"
#
# result7 = f"{w1} {W2} {W3} {W4} {W5}"
# print(result7)

print()
print("-"*50)
str7 = "we are learning python programming"

print(str7[0:34:2])
print(str7[::-1])

w1 = str7[0:2]
w2 = str7[3:6]
w3 = str7[7:15]
w4 = str7[16:22]
w5 = str7[23:]

result2 = f"{w1} {w2}{w3}{w4}{w5}"
print(result2)

W1 = f"{w1[::-1]}"
W2 = f"{w2[::-1]}"
W3 = f"{w3[::-1]}"
W4 = f"{w4[::-1]}"
W5 = f"{w5[::-1]}"

result5 = f"{W1} {W2} {W3} {W4} {W5}"

print(result5)

##############

print(dir(str))


# # 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
 #'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
 #'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
# # 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
# # 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace',
# # 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# # 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
#upper', 'zfill'
#

print()
print("-"*50)
list1 = "Hello This Is SatYa"

print(list1.upper())
print(list1.lower())
print(list1[3].upper())
print(list1[6].lower())

str_b = "hello i am learning python"

str_c = str_b.replace("i", "we")
print(str_c)

str_d = "hai"
str_e = str_d.islower()
print(str_d.upper()) # HAI
print(str_e) # true



print()
print("-"*50)

str_f = "HellO I AM leArning pythOn"

output = str_f.title()
print(str_f.title()) # Hello I Am Learning Python

print(str_f.istitle()) # False
print(output.istitle()) # True

print(str_f.upper()) # HELLO I AM LEARNING PYTHON

print(str_f.lower()) # hello i am learning python

print(str_f.replace("I", "we")) # HellO we AM leArning pythOn


print()
print("-"*50)

str_g = ("hello my name is satya and i am from"
         " visakapatnam and my father name is raju and my mother name is satyavathi")

print(str_g.count("my"))  # 3
print(str_g.count("a"))  #18
print(len(str_g))  # 109


print()
print("-"*50)

str_h = " hAi I aM From AndHra"

print(str_h.swapcase()) # HaI i Am fROM aNDhRA


str_i = "hi my name is satya"
temp = ""
for i in str_i:
    if i not in temp:
        print(i, end="")
        print(i, str_i.count(i))
        temp = temp+i
print(str_i.index("i"))
print(str_i.index("a"))
print(str_i.find("is"))

print(str_i.split(" ")) # ['hi', 'my', 'name', 'is', 'satya']


print()
print("-"*50)
#5. write a python program to second largest word from given string.
str_p = "Hello We Are Learning Python"
output = "Python"

max_len = 0
longest_word = " "
word_list = str_p.split()

for word in word_list:
    word_len = len(word)
    if word_len > max_len:
        max_len = word_len
        longest_word = max_len
    else:
        continue


print(longest_word)


satya = "hello i am learning python but its very difficult to understand for me"

max = 0
long = ""
satya_list = satya.split()

for i in satya_list:
    i_len = len(i)
    if i_len > max:
        max = i_len
        long = max
    else:
        continue
print(long)

print("-"*50)
str10 = ("satya 9490570891 chsatya@gmail.com ")

str10_list = str10.split()

for word in str10_list:
    if "@" in word:
        print("mail id:", word)

satya1 = "123dsesgse"
print(satya1.isalnum()) # True









