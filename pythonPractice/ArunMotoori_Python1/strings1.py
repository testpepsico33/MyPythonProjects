#multiple ways to store string
first_name="Nirmal"
last_name='CJ'
location=str("Bangalore")

print(first_name)
print(type(first_name))
print(last_name)
print(type(last_name))
print(location)
print(type(location))

#String work lik collection "list" in python
name="kavin"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4]) #printing each value of the string
print("Using forloop")
for i in name:
    print(i)
#size of string
print(len(name))
for k in range(len(name)): #len(name)=5 , k=0,1,2,3,4 ->5 iteration
    print(name[k])
# in and not in operator
print("vin" in name)
print("vin" not in name)
print("Nir" in name)
print("Nir" not in name)
#slicing
print(name[1:3]) #index : position
print(name[1:]) #index : last position
print(name[:5]) #first index :position
print(name[:]) #first index : last position
#Modifying string
print(name.upper())
print(name.lower())
name="        kavin kumar         "
print(name.strip()) #remove the leading and trailing whitespace of string but not the in between 2 string
name="kavin kavin"
print(name)
print(name.replace("k","r"))
#spliting string
name="My name is kavin Kumar"
words=name.split(" ") #split return type is list
print(words)
print(type(words))
print(words[2])
for word in words:
    print(word)
name="My-name-is-kavin-Kumar"
print(name.split("-") )
#Strings are immutable
name="kavin" # name variable pointing to memory location where "kavin" is stored
print(id(name)) #fetch the memory location id of kavin
name="ravin" # name variable pointing to memory location where "ravin" is stored
print(id(name)) #fetch the memory location id of ravin
#note: externally string looks like mutable internally its unmutable
#Other string functions
name="my name is kavin kumar"
print(name.capitalize()) #only first word of the string capatilized
print(name.title()) #each and every first word of string is capatilized
name="My name is Nirmal Kumar. I teach Python. Python is easy to learn"
print(name.count("Python")) #return the count of number of times the given word is repeated
print(name.find("Python")) #corss check with string the required word is present or not
print(name.find("java")) #return -1 if the given word is present in the string
#Comparing the strings in python
name_one="Kavin"
name_two="kavin"
name_three="ravin"
print(name_one==name_two)
print(name_one==name_three)

print(name_one.__eq__(name_two))
print(name_one.__eq__(name_three))

print(name_one.casefold() == name_two) #when we just want to compare string without case sensitive
#in and not in operator
#LIST
colour=["green","red","blue"]
print(colour)
print("green" in colour)
print("yellow" not in colour)
#TUPLE
colour=("green","red","blue")
print(colour)
print("green" not in colour)
print("yellow" not in colour)
#SET
colour={"green","red","blue"}
print(colour)
print("green" in colour)
print("yellow" in colour)
#for loop and for each loop
colour={"green","red","blue"}
for i in range(11):
    print(i)
for color in colour:
    print(color)
#using string
a="python is a easy programming language"
print("python" in a)
print("python" not in a)
print("java" in a)
print("java" not in a)