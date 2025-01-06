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
append_content_to_file("append_data_new.txt", "We are Learning Python Programming")
