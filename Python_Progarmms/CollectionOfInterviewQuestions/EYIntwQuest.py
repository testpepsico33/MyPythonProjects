
input_str="Test automation at mindtree"

words=input_str.split()
#By default "split()" splits the string at spaces and returns a list of words
# after this word will be ['Test', 'automation', 'at', 'mindtree']
print(words)
print(type(words))
reversed_words= [word[::-1] for word in words]

print(reversed_words)
print(type(reversed_words))

output_str=' '.join(reversed_words)
#The join() method is used to concatenate the list of reversed words into a single string

print(output_str)




