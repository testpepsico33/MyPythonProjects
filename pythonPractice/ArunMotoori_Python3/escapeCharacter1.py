
#\'
a=('My name is \'nirmal\'. I teach \'python\' programming')
print(a)
#\"
a=("My name is \"nirmal\". I teach \"python\" programming")
print(a)

#If we add single/double quote inside single/double quote will throw an error instead we can use \' and \" to overcome it

#\\ -->To add slash between the character use double slash so that single slash displayed in the output
a=("My address is 3\\4\\5-3-2")
print(a)
#\n --> Spliting words in to next line
a=("My name is Nirmal.\nI teach python programming")
print(a)
#\r -->Words will be printed after the slash r before the \r statement is ignored
a=("My name is Nirmal.\rI teach python programming")
print(a)
#\t -->Tab space
a=("My name is Nirmal.\tI teach python programming")
print(a)
#\b -->Back space
a=("My name is Nirmal.\b\b\bI teach python programming")
print(a)