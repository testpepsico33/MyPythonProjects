
input_str="Test Automation At Mindtree"

words=input_str.split()

print(words)

reverse_str_words= [word[::-1] for word in words]

print(reverse_str_words)

output_string=''.join(reverse_str_words)
print(output_string)
