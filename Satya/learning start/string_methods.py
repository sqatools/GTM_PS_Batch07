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
print(str5[1:-1])

result4 = f"{v}virat{t} {i}is{s} {b}best{t} {i}india{a} {p}player{r}"
print(result4)


v = "virat"
i = "is"
b= "best"
p = "player"

result6 = f"v{v}t i{i}s b{b}t p{p}r"
print(result6)


str = "i am a good boy"

w1 = str[0:1]
w2 = str[2:3]
w3 = str[4:5]
w4 = str[6:10]
w5 = str[11:14]

W2 = f"{w2[0]}{w2}{w2[-1]}"
W3 = f"{w3[0]}{w3}{w3[-1]}"
W4 = f"{w4[0]}{w4}{w4[-1]}"
W5 = f"{w5[0]}{w5}{w5[-1]}"

result7 = f"{w1} {W2} {W3} {W4} {W5}"
print(result7)

