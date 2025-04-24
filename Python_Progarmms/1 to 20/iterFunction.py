
l=[9,6,5,3]

itr=iter(l)

print(next(itr))
print(next(itr))
print(next(itr))

#Iterator
from typing import Iterator, Iterable, Generator

people: list[str] =['bob','james','luigi','nirmal','kumar','arav','nandhini']
people_iter:Iterator[str]= iter(people)

print(next(people_iter))
print(next(people_iter))
print(next(people_iter))
#print(list(people_iter)) #already 3 values exhausted

for i in range(2):
    print(next(people_iter)) #this will return the remaining values

#generator
def my_generator(n):
    for i in range(n):
        yield i

for value in my_generator(5):
    print(value)

#Iterable

