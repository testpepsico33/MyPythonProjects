#creating tuple
a=(9,6,5,4,3)
print(a)
print(type(a))
print(a[2])

#forward and backward indexing
b=(7,1,3,5,6)
print(b[2]) #Forward indexing
print(b[-2]) #5-2=3 Backward indexing

#finding the length of tuple
c=(1,2,3,4,5)
print("Length of tuple")
print(len(c))

#forloop using tuple
d=(5,7,9,3)
for i in range(len(d)):
    print(i)
    print(d[i])

#foreachloop using tuple
each=(3,7,9,6,5)
for e in each:
    print(each)
    print(e)

# slicing tuple
f=(7,9,6,3,2)
print(f[1:3]) # index : position
print(f[:4]) #0 index : fourth position
print(f[2:]) #2nd index : last position

#using "in" and "not in" operator in tuple
g=(7,6,9,4,5)
print(4 in g)
print(14 in g)
print(5 not in g)

#Note:count(), sum(), min(), max(), index(), del a, type()
h=(9,3,3,4,5,6,1,2)
print(h.count(3))
print(sum(h))
print(min(h))
print(max(h))
print(h.index(1))
print(type(h))
k=(2,3,(5,7,9),4,6,9)
print(k[2])
print(k[2][2])
j=(1,2,2,2,2,2,2,2)
print(j)
#del j
#print(j)

#list inside the tuple is mutable
l=(2,3,[5,7,9],4,6,9) #only the list inside the tuple is mutable
print(l) #before update
l[2][0]=6
print(l) #after update

#converting string to tuple
m=tuple("goOgle")
print(m[2])

for e in m:
    print(e)
    print(m)
