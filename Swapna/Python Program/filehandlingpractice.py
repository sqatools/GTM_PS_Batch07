# Python Program How to read a file in reading mode

# with open("testfile.txt","r") as file:
#     print(file.read())
#


#Python file program to overwrite the existing file content.

# with open("testfile.txt","w") as file:
#     file.write("test")
#


#Python file program to append

# def appendfile(filepath):
#     with open(filepath,"a") as file:
#         file.write("testdndfdj hfdkjfhkjdhkjd")
#
#
# appendfile("testfile.txt")


# Python file program to get the file’s first three and last three lines.

# def first_last_theree(filepath):
#      with open(filepath,"r") as file:
#          line = file.readlines()
#
#          for l in range(3):
#            print([line[l]])
#
#
#
# first_last_theree("testfile2.txt")
#
#
# def find_email_id_email(filepath):
#     with open (filepath,"r") as file:
#         content = file.read()
#         print(content)
#
#     word_list = content.split(" ")
#     print(word_list)
#     for word in word_list:
#         if '@' in word:
#             print(word)
#
# find_email_id_email("email.txt")


# # Python file program to get a specific line from the file.
#
# def read_no_lines(filepath, no_lines):
#     file = open(filepath, "r")
#     lines= file.readlines()
#     print(lines[0])
#
#
#
# read_no_lines("testfile2.txt",5)


#Python file program to get odd lines from files and append them to separate files.

def oddline_fromfile(filepath1,filepath2):
    with open(filepath1,"r") as file1:
       file1_read= file1.readlines()

    with open(filepath2,"a")as file2:
         for l in range(len(file1_read)):
            if l+1 ==0:
             file2_read= file2.write(file1_read[l])


oddline_fromfile("testfile2.txt","testfile.txt")


