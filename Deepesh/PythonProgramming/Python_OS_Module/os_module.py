import os
import shutil
import sys

########################
# get current working directory
print("current directory :", os.getcwd())
# E:\Trainings\GTM_PS_Batch07_22Nov24\GTM_PS_Batch07\Deepesh\PythonProgramming\Python_OS_Module

# change the working
"""
os.chdir("E:\\Filesdata")
print("current directory :", os.getcwd())
"""

####  create a directory on local system ####
# os.mkdir("folder1") # create folder
# os.rmdir("folder1")  # remove folder


### create multi level directories #########
# create multi level directory
# os.makedirs("E:\\Filesdata\\batch07\\f1\\f2\\f3\\f4")

# remove all directories
# removedir, will only remove the empty directories
# os.removedirs("E:\\Filesdata\\batch07\\f1\\f2\\f3\\f4")


####  rename folder #############

# create folder
#os.mkdir("folder1")

# rename the folder
# os.rename("folder1", "updated_folder")


############### Get list of files and folder from target directory ###############
tar_path = "E:\\Filesdata"
data_list = os.listdir(tar_path)
print(data_list)


for data in data_list:
    print(data)

###### join path using os.path.join() method ##########
tar_path = "E:\\Filesdata"
file_name = "count_name.txt"
file_path = os.path.join(tar_path, file_name)
print("file path :", file_path)

#### Check given path is file or folder #########

path1 = "E:\\Filesdata\\count_name.txt"
path2 = "E:\\Filesdata\\batch07"
path3 = "E:\\Filesdata\\test_file_name.txt"

print("_"*50)
# check file/folder exist on the target location or not
print("path1 exist :", os.path.exists(path1)) # True
print("path2 exist :", os.path.exists(path2)) # True
print("path3 exist :", os.path.exists(path3)) # False


# Check given path is file or folder
print("check path1 is file :", os.path.isfile(path1)) # True
print("check path2 is file :", os.path.isfile(path2)) # False
print("check path2 is folder :", os.path.isdir(path2)) # True

print("_"*50)
############## get all the files from target location and count files/folder #############
tar_path = "E:\\Filesdata"
data_list = os.listdir(tar_path)

file_count = 0
dir_count = 0
for data in data_list:
    data_path = os.path.join(tar_path, data)

    # append file/folder path to the file
    with open("files_data.txt", "a") as file:
        file.write(f"{data_path}\n")

    # check the path is file or not
    if os.path.isfile(data_path):
        file_count += 1
     # check the path is folder or not
    elif os.path.isdir(data_path):
        dir_count += 1


print("files count :", file_count) # 38
print("folder count :", dir_count) # 15


print("_"*50)
############## Check the size of the file ###########
file_path = "E:\\Filesdata\\count_name.txt" # 980
print("get file size", os.path.getsize(file_path)) # 980 bytes
print("get modified time", os.path.getmtime(file_path)) # 1670932252.810281
print("get creation time", os.path.getctime(file_path)) # 1653020213.4924054


print("_"*50)
############## Copy file from one directory to another ###########
file_path = "E:\\Filesdata\\count_name.txt"
tar_path1 = "E:\\Filesdata\\batch07\\count_name.txt"
tar_path2 = "E:\\Filesdata\\batch07\\count_name_updated.txt"
# copy with same name
shutil.copy(file_path, tar_path1)
shutil.copy(file_path, tar_path2)


print("_"*50)
################# Run windows command ##################
# os.system("control")  # open control panel
# os.system("notepad.exe") # open new notepad window.
os.system("python test_script.py")  # run python script from python file

print("_"*50)
####### Get CPU count of your machine ####
print("CPU count :", os.cpu_count())
# CPU count : 8


######### get platform name ##########
print("platform name :", sys.platform) # win32
print(sys.version_info)
# sys.version_info(major=3, minor=12, micro=2, releaselevel='final', serial=0)

print(sys.version)
# 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
