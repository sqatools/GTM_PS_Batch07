
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
