def hello():
    print("good morning")

hello()
# good morning

def greeting_msg(msg):
    print(msg)

greeting_msg('hello i am learning python')

# hello i am learning python

var1 = "hello my name is satya"

greeting_msg(var1)
# hello my name is satya

def addition(n1, n2, n3):
    print(n1+n2+n3)

addition(24, 25, 26) # 75

x, y, z = 20, 30, 40
addition(x, y, z) # 90


def values(a1, a2, a3 = 6):
    add = a1+a2
    sub = a1-a2
    multi = a2*a3
    divid = a3//a1
    print(add, sub, multi, divid)

values(2, 3) # 5 -1 18 3


def add_values(a = str, b = str, c= str):
    print(a+b+c)
add_values("hello ", "we are ", "learning python")

print("-"*50)

def write_content(filepath, content):
    obj_path = open(filepath, "w")
    data = obj_path.write(content)
    print(data)
    obj_path.close()

str1 = "hello we are learning python programming. if i practise more it will easy to learn, otherwise it is very difficulty to learn"

write_content("write_content_file.txt", str1)

def append_content(filepath, content):
    obj_path = open(filepath, "a")
    data = obj_path.write(content)
    obj_path.close()


append_content("new_append_file.txt", "hello how are you. i am good")

append_content("write_content_file.txt", "namaste, i am adding new content to this file then i will check the data is added or not")

append_content("write_content_file.txt", "i want to learn python then i will work on python then "
                                         "after i will give interview on bosch and i "
                                         "will get good package and security")

def write_content_file(filepath, word1, word2):
    with open(filepath, "r") as filepath
        file_data = filepath.read()






