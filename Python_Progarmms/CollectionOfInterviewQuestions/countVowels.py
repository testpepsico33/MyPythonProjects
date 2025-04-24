"""Counts the number of vowels (a, e, i, o, u) in a given string."""
word = "Hello"
vowels = "aeiouAEIOU"
vowel_count = 0

for char in word:
    if char in vowels:
        vowel_count +=1
print(vowel_count)
