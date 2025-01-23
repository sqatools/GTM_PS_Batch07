def read_file(filepath):
   file_obj = open(filepath, "r")
   data = file_obj.read()
   words = data.split()
   data_list = data.split(" ")
   output = []
   for word in data_list:
      if "@" in word:
         output = data_list.append("@")
      else:
         continue
   print(output)
   file_obj.close()

read_file("NewFile.txt")

