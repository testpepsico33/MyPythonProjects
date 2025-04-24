string = "nirmalkumar"
char_counts = {}

# Count character occurrences
for char in string:
    if char in char_counts:

        char_counts[char] += 1
    else:
        char_counts[char] = 1

# Find the first non-duplicate character
for char in string:
    if char_counts[char] == 1:
        print(char)
        break  # Stop after finding the first one
else: #this else belongs to the for loop.
    print("No non-duplicate character found.")