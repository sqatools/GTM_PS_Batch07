def get_maximum(lst):
    return max(lst)
L1 = [4, 6, 89, 22, 55, 44]
output = get_maximum(L1)
print("Maximum value:", output)

print("_"*50)

def count_vowels(s):
    vowels = 'aeiou'
    s = s.lower()
    vowel_count = {}
    for char in s:
        if char in vowels:
            vowel_count[char] = vowel_count.get(char, 0) + 1
    return vowel_count

str1 = "Hello Good Morning"
output = count_vowels(str1)
print("Vowel count:", output)

print("_"*50)

def get_maximum(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

L1 = [4, 6, 89, 22, 55, 44]
output = get_maximum(L1)
print("Maximum value:", output)
