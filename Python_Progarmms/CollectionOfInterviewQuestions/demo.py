
input_string="Hello world"
char_count={}

for char in input_string:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
print(char_count)

string_input="Test automation at mindtree"

words=string_input.split()

print(words)

reversed_string= [word[::-1] for word in words]

print(reversed_string)

output_string=''.join(reversed_string)

ip_string="mississippi"

result=""

for char in ip_string:
    if char not in result:
        result=result+char
print(result)
