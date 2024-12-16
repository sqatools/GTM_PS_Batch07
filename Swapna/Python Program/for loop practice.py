#erite a python program to print 1 to 100

# for i in range(1,100):
#     print(i)


#print the odd values from 1 to 20

for i in range(1,20):
    if i%2!=0:
        print(i)

str1 = "virat is best india Played"
print(str1[2:25])


# str1 = We are learning Python Programming
# 1. swap first and last character of each word
# 2. Reverse each word of a string

str1 = "We are learning Python Programming"
w1=str1[0:2]
print(w1)
w2=str1[3:6]
print(w2)
w3=str1[7:15]

print(w3)
w4=str1[16:22]
w5=str1[23:]
print(f"{w1[::-1]} { w2[-1]}{w2[1:-1]}{w2[0]} {w3[-1]}{w3[1:-1]}{w3[0]} {w4[-1]}{w4[1:-1]}{w4[0]} {w5[-1]}{w5[1:-1]}{w5[0]}")

# 2. Reverse each word of a string # str1 = We are learning Python Programming
print(f'{w1[::-1]} {w2[::-1]} {w3[::-1]} {w4[::-1]} {w5[::-1]}')





