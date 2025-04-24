words = ["apple", "banana", "cherry"]  # Example list of words

# Step 1: Reverse each word in the list
reversed_words = []
for word in words:
    reversed_word = word[::-1]
    reversed_words.append(reversed_word)

# Step 2: Print the list of reversed words
print(reversed_words)