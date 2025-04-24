import random

#random()
print(random.random()) # in between 0 and 1 floating point value will be printed
print(random.random()*100) # in between 0 and 100 floating point value will be printed
print(int(random.random()*100)) # in between 0 and 100 int value will be printed
print(int(random.random()*500)) # in between 0 and 500 int value will be printed

#randint()
print(random.randint(1,1000)) #in between 1 to 1000 integre value will be printed
print(random.randint(1,5)) #in between 1 to 5 integre value will be printed

#randrange()
#Last value of the range is not considered
print(random.randrange(1,5)) #in between 1 to 4 int value will be printed
print(random.randrange(33,66)) #in between 33 to 65 int value will be printed