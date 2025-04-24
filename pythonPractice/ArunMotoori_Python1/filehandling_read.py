
file=open("C:\\Users\\nimalkumar.j\\PycharmProjects\\pythonPractice\\Files\\python.txt","r")

#print(file.read()) #All character will be read here
#print(file.read(15)) #15 character will be read here
#print(file.readlines()) #read all lines in the list format
#print(file.readline()) #read line by line but only one line, first line in the text file is printed
"""
print(lines) #gives us the list of values even its in seperate lines
for line in lines:
    print(line)
file.close()
"""
lines=file.readline()
print(lines)
print(lines)
file.close()
