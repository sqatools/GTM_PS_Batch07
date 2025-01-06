from math import factorial

print(dir(tuple))

# count', 'index'

tup1 = ("hello i am learning python")

print(tup1, type(tup1))
# hello i am learning python <class 'str'>

tup2 = (1, 2, 3, 4)
print(type(tup2))
# <class 'tuple'>

tup3 = ("hello", 3, 4, 6, (1, 3, 5, 7), {89 : 1, 45 : 2, 23 : 3}, [56, 34, 65], 76)

print(tup3[-1]) # 76
print(tup3[6][2]) #  65
print(tup3[-3][45]) # 2
print(tup3[0]) # hello

print(tup3[::-1])
# (76, [56, 34, 65], {89: 1, 45: 2, 23: 3}, (1, 3, 5, 7), 6, 4, 3, 'hello')

tup4 = (3, 4, 5, 6, 7)

for val in tup4:
    print(val)

for num in range(len(tup4)):
    print(num, tup4[num])

print("-"*50)

tup5 = (1, 3, 5,6, 7, 3, 65, 56, 2, 3, 1, 7)

print(tup5.count(3))
print(tup5)

print(tup5.index(5))

print(sorted(tup5))
# [1, 1, 2, 3, 3, 3, 5, 6, 7, 7, 56, 65]

print(tuple(reversed(tup5)))


tup6 = (345, 65,7, 34, 7,6, 123, 657, 987)
print(max(tup6))
print(min(tup6))
print(sum(tup6))


print()
tup_11 = (3, 6, 8, 5, 12, 4)
# output = factorials list
output = []

for val in tup_11:
    fact = 1
    for i in range(val, 0, -1):
        fact = fact*i

    output.append(fact)

print("Factorial output :", output)

print()
tup8 = (3, 5, 6, 8)
output = []
for val in tup8:
    fact = 1
    for i in range(val, 0, -1):
        fact = fact*i
        output.append(fact)
print(output)



def vowels(char):
    char = "a, e, i, o, u"
    print((char.count(char)))

str1 = "hello we are learning python"


# 1. write a python program to get maximum from given list using function
list1 = [4, 6, 89, 22, 55, 44]
# output = 55

#
# def read_file(filepath):
#     file_obj = open(filepath, "r")
#     data = file_obj.read()
#     print(data)
#     file_obj.close()
#
# read_file("newfile.txt")
#
# def write_file(filepath):
#     file_obj = open(filepath, "w")
#     data = filepath.write()
#     print(data)
#     filepath.close()
#
# write_file("new_python_file.py")
#
# def append_file(filepath):
#     file_obj = open(filepath, "a")
#     data = file_obj.append()
#     print(data)
#     file_obj.close()









