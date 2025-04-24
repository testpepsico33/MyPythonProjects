
#def remover_duplicate_char():
input_string="mississippi"
result=""

for char in input_string:
    if char not in result:
        result=result+char
print(result)

input_string1="mississippi"
seen_characters = set() #Empty set assign it to the variable seen_character
result = ""
for char in input_string1:
    if char not in seen_characters: #
      seen_characters.add(char)
      result += char
print(seen_characters)
print(result)

Str="Hello World"
char_count={}
for char in Str:
    if char in char_count:
        char_count[char]+=1 #{}
    else:
        char_count[char]=1 #{'H':1,'e': 1,'l':1,'}