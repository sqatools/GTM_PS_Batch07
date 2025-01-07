# seek(byte, offset) method : seek method help to move the cursor position in difference position in the file
# seek(20, 0) :  when we set offset val is zero then cursor will be set with respect the offset from begining of the file.
# seek(20, 1) : when we set offset value is one then reference of cursor position will be current
#               position of the cursor not begining of the file

# seek(20, 2) :  When we set offset value is 2 then the reference cursor position is end of the file.
# tell() method : Tell method provide the current position of the cursor


# # seek(20, 0) :  when we set offset val is zero then cursor will be set with respect the offset from begining of the file.
def seek_data_with_offset_zero(filepath):
    with open(filepath, "r") as file:
        print("initial cursor position :", file.tell())
        file.seek(30, 0)
        print("new cursor position :", file.tell())
        data = file.read()
        print(data)


#seek_data_with_offset_zero("read_data.txt")

# seek(20, 1) : when we set offset value is one then reference of cursor position will be current
# #               position of the cursor not begining of the file
def seek_data_with_offset_1(filepath):
    with open(filepath, "rb") as file:
        print("initial cursor position :", file.tell())
        char_40 = file.read(40)
        print("40 char :", char_40)
        print("new cursor position :", file.tell())
        print("_"*50)
        file.seek(30, 1)
        print("new cursor position :", file.tell())
        print("_"*50)
        data = file.read()
        print(data)


#seek_data_with_offset_1("read_data.txt")


# seek(20, 2) :  When we set offset value is 2 then the reference cursor position is end of the file.
def seek_data_with_offset_2(filepath):
    with open(filepath, "rb") as file:
        file.seek(-50, 2)
        # read last 5o character from file
        data = file.read()
        print(data)

seek_data_with_offset_2("read_data.txt")
