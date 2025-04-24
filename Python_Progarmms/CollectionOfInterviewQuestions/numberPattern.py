
input_str = input("Enter a string: ")

words = input_str.split()

reverse_words = words[::-1]

print(reverse_words)

output_words = []
for word in reverse_words:
    output_words.append(word[::-1])

output_str = " ".join(output_words)
print("Output:", output_str)