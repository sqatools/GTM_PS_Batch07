"""
# file mode to open
1. read mode (r): read mode help to read content of the file.
2. write mode (w): write mode help add new content to the file. but it overwrite the previous content
3. append mode (a): append mode help to append content to the file, and add content at end of the file.
"""

# Read content of any text file
def read_file(filepath):
    file_obj = open(filepath, "r")
    data = file_obj.read()
    print(data)
    file_obj.close()

# read current location file
read_file("read_data.txt")

# Try to read non available file
# read_file("read_data1.txt")
# FileNotFoundError: [Errno 2] No such file or directory: 'read_data1.txt'

# Read file from other location
# read_file("E:\\Filesdata\\count_name.txt")


##########################################
# Write content to the file

def write_content(filepath, content):
    file = open(filepath, "w")
    file.write(content)
    file.close()


# 1. write content to non-existing file : In this case it will create new file with provided name
#   update the content
"""
str1 = "Hello Good Morning, Hope You are doing good."
write_content("write_data.txt", str1)
"""

#2. write content to existing file : In this case write method will overwrite the
#   previous content of existing file
"""
str1 = "Hello Good Morning, Hope You are doing good."
write_content("write_data_new.txt", str1)
"""


##########################################
# Append content to the file

def append_content_to_file(filepath, content):
    file = open(filepath, "a")
    file.write(content)
    file.close()

# 1. Append content to non-existing file:
#    In this case, append mode will create new file with the name provided and
#    add content to file
# append_content_to_file("append_content.txt", "We are Learning Python Programming")


# 2.  Append content to existing file
#     In this case, append mode will add content to existing file at the end file
#     without replacing the previous content
append_content_to_file("append_data_new.txt", "\nWe are Learning Python Programming")


print("_"*50)
################################
# different level of read file content
# 1. read specific number of bytes
# 2. read specific number of lines from file
# 3. read list of lines or specific line

# 1. read specific number of bytes
def read_byte_data(filepath, no_bytes):
    file = open(filepath, "r")
    data = file.read(no_bytes)
    print(data)

#read_byte_data("read_data.txt", 20)
#read_byte_data("read_data.txt", 50)



# 2. read specific number of lines from file

def read_no_lines(filepath, no_lines):
    file = open(filepath, "r")
    for i in range(no_lines):
        print(file.readline(), end="")
    file.close()

#read_no_lines("read_data.txt", 4)



# 3. read list of lines or specific line
def read_list_of_lines(filepath, line_no):
    file = open(filepath, "r")
    lines_list = file.readlines()
    print(lines_list)
    print(lines_list[line_no-1])
    print("is file close :", file.closed)
    file.close()
    print("is file close :", file.closed)

# read_list_of_lines("read_data.txt", 3)


##################################################
# context manager :  through the context manager we can open and close file internally, so no need
#                    to close the file explicitly.

def read_file_context(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        print(data)
        print("is file closed :", file.closed)

    print("is file closed :", file.closed)

read_file_context("read_data.txt")
###################################################

# write a python program to replace the specific word in given file
def replace_word_in_file(filepath, word1, word2):
    with open(filepath, "r") as file:
        file_data = file.read()

    updated_data = file_data.replace(word1, word2)

    with open(filepath, "w") as file2:
        file2.write(updated_data)


#replace_word_in_file("read_data.txt", "JAVA", "PYTHON")


# write a python program to take lines two different files and append to third file.

def read_two_file_add_to_third_file(file1, file2, file3):
    # read file1 data
    with open(file1, "r") as file1_obj:
        file1_data = file1_obj.read()

    # read file2 data
    with open(file2, "r") as file2_obj:
        file2_data = file2_obj.read()

    # append file1_data and file2_data to file3
    with open(file3, "a") as file3_obj:
        file3_obj.write(file1_data)
        file3_obj.write(file2_data)


#read_two_file_add_to_third_file("file1.txt", "file2.txt", "file3.txt")

# Class work
# write a python program to get all the emails from the given file
# 1.  read file data
# 2.  split the content to get word list
# 4.  go through each word using loop
# 3.  check @ in each word and print the word
