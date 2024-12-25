# #4. Write a python program to get email and phone number from given string
#
# str1 = " Hello python 8989898787 test@gail.com 5654645645 user2@tahoo.com Hope doing good"
#
# word_list = str1.split(" ")
# print(word_list)
#
# phone_numbers = []
# emails = []
#
# # for word in word_list:
# #     if word.isdigit() and len(word) == 10:
# #         phone_numbers.append(word)
# #     elif  '@' in word and ".com" in  word :
# #         emails.append(word)
# #
# #
# #
# # print("phone number : ", phone_numbers)
# # print(" emails", emails)
#
# for word in word_list:
#     if word.isnumeric and len(word)==10:
#         print(word)
#     elif '@' in word and ".com" in word:
#         print(word)
#
#
#
# print("phone number : ", phone_numbers)
# print(" emails", emails)
#
#
# str_p = "Hello We Are Learning Python"
# output = "Python"
# maxlen = 0
# nextlen = 0
# longword = ""
# nextword = ""
# wordlist = str_p.split(" ")
#
# for word in wordlist:
#     wordlen = len(word)
#     if wordlen > maxlen:
#         maxlen = wordlen
#         longword = word
#     elif maxlen > wordlen >nextlen:
#         nextlen = wordlen
#         nextword = word
#
# print("Second longest word: ", nextword)


# HW1 :  write a python program to second last max value from given list
# list1 = [4, 6, 22, 77, 23, 44, 66, 100]
# output = 77
#
#
# largest_num = 0
# seclarge_num = 0
# for val in list1:
#     if val > largest_num:
#         seclarge_num =largest_num
#         largest_num = val
#
#     if val < largest_num and val > seclarge_num:
#         seclarge_num = val
#
#
# print("seclarge num", seclarge_num)

# HW2 :  write a python program to move all positive value in left side of the list
# and negative to right side of the list

# output = [4, 7, 8, 44, -2, -11, -7, -22]

# l = [4, 7, -2, 8, -11, 44, -7, -22]
#
# n = len(l)
# print(" orginal list", l)
#
# for i in range(n-1):
#      for j in range(n-i-1):
#           if l [ j ] <0:
#                 l [ j ], l [ j + 1] = l [ j + 1], l [ j ]
#
# print("After shifting list is:", l)



list = [4, 7, -2, 8, -11, 44, -7, -22]


#

list = [4, 7, -2, 8, -11, 44, -7, -22]
list_len = len(list)
j =0
for i in range(list_len):
    #print(i)
    if list[i] >0:

          temp = list[i]
          list[i] = list[j]
          list[j] =temp
          j = j+1


print("out",list)