
######################## 1. swap each letter of string ##################333

def swap_first_and_last_characters(sentence):

    words = sentence.split()


    swapped_words = []
    for word in words:
        if len(word) > 1:

            swapped_word = word[-1] + word[1:-1] + word[0]
        else:

            swapped_word = word
        swapped_words.append(swapped_word)


    return ' '.join(swapped_words)



sentence = "we are learning python programming"
result = swap_first_and_last_characters(sentence)
print(result)     #ew era gearninl nythop grogramminp

############################## 2. reverse each word of the srtring  #####################################3

def reverse_word_in_string(s):
    words = s.split()
    reversed_words = [words[::-1] for word in words]
    return '' .join(reversed_words)

    input_string = "we are learning python programming"
    result = reverse_word_in_string(input_string)

    print(result)  ##ew era gearninl nythop grogramminp


#####################title() method############################

str_g = "HeY hope yoU Are DOing Good"
print("str_g :" , str_g.title())
###Hey Hope You Are Doing Good
print("Istitle for str_g :", str_g.istitle())## False




print("_"*50)
############################################
# count() method: this method count the occurrences of any character or substring in the given string



str_j = " lets Hope India will win the last test India Match"
print("count of l :", str_j.count("l"))
print("count of India :", str_j.count("India"))

print("_"*50)

###########################################
# swacase() method: this method covert


str_k = "Lets HopE India will win the Test India Match"
print("swap case of str_k :", str_k.swapcase())

##lETS hOPe iNDIA WILL WIN THE tEST iNDIA mATCH


########################################
# index() method :

str_x = "Good Morning"
print("index of M :", str_x.index("M"))#index of M : 5

####################################
#fine method :

str_q = "Hello Python Programming"
print(str_q.find("Python"))# 6



print(str_q.find("Good")) #-1


#############################################
#split method

str_p = "Python#Programming#Is#Easy#To#Learn"
result = str_p.split("#")
print("split result :", result)

# ['Python', 'Programming', 'Is', 'Easy', 'To', 'Learn']





















































































































