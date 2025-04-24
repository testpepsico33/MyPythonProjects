input_string="Hello World"
char_counts = {}
for char in input_string:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1
print(char_counts)

text = "hello"
char_counts = {}

for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1 # h:0+1-1,e:0+1-1,l:0+1-1,l:1+1-2,o:0+1-1

print(char_counts)