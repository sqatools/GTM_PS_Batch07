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

