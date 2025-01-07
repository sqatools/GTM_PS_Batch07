# #file = open("testfile.txt", "x")
#
#
# #write into file
#
# file = open("testfile2.txt","w")
# file.write(" Hi this is swapna i am learing python automation \n testing for second file ")
# file.close()
#
# #read file
#
# file = open("testfile2.txt","r")
# print(file.read())
# file.close()

#append file
file = open("testfile2.txt", "a")
file.write("testing for appending")
#print(file.read())
file.close()


with open("testfile2.txt", "r") as file:
    print(file.read())

#Program to get the file’s first three and last three lines

with open("testfile2.txt","r") as file:
     lines = file.readlines()
     print(lines)
     for i in range(len(lines)):
         print(lines[i])




# Class work
# write a python program to get all the emails from the given file
# 1.  read file data
# 2.  split the content to get word list
# 4.  go through each word using loop
# 3.  check @ in each word and print the word


def find_email_id_email(filepath):
    with open (filepath,"r") as file:
        content = file.read()
        print(content)

    word_list = content.split(" ")
    print(word_list)
    for word in word_list:
        if '@' in word:
            print(word)

find_email_id_email("email.txt")

