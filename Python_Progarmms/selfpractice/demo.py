#each char count
input_string="nirmalkumarnirmalkumar"

char_count={}

for char in input_string:
    if char in char_count:
        char_count[char] +=1
    else:
        char_count[char] =1
print(char_count)

#countVowels
word="nirmal"
string_vowels="aeiouAEIOU"
vowels_count=0

for vowels in word:
    if vowels in string_vowels:
        vowels_count+=1

print(vowels_count)

#Max_Min
list=[1,33,55,99,42,32,23]

max_num=list[0]
min_num=list[0]

for num in list:
    if num > max_num:
        max_num =num
print(max_num)

#Reverse string of each character



