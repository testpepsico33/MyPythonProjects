#creating set
a={9,1,5,7}
print(a) #set is unordered so output is displaying in random order{9, 5, 1, 7}
#un-index
b={9,1,5,6}
#print(b[2]) #TypeError: 'set' object is not subscriptable
#Duplicate value
c={9,1,5,9,6,9}
print(c) #ignoring duplicate values {9, 5, 1, 6}
#finding the type and length of set
d={5,9,6,1,3,2}
print(type(d))
print(len(d))
#adding values into the set
e={1,2,3,4}
print(e) #before add
e.add(5)
e.add(6)
print(e) #after add
#updating values into the set
f={9,7,6,5}
print(f) #before
f.update([2,4,1,99]) #update function in a single go helps to update the multiple values
print(f) #after
#remove,pop and discard value from set
g={7,8,9,1,3}
print(g) #before
g.remove(8)
g.discard(15) #15 is not present in set instead of giving error discard fun ignore the error
g.pop()
print(g) #after
#clear
h={12,13,14,15}
print(h)
h.clear() #removing all the values from set
print(h)
#delete
i={18,8,44,17}
print(i) #befor del
del i
#print(i) #after del
# for loop not able as there is indexing we can use for each loop
j={55,66,77,99}
for ee in j:
    print(ee)
    print(j)
#using "in" and "not in" operator
k={2,3,4,5}
print(2 in k)
print(3 not in k)
print(66 in k)
#only "tuple" can be inside a set , not set inside set and set inside list
#l3={2,(2,3,4),5,6,7} #tuple can inside a set
#l1={1,[2,3,4],5,6,7} #not list
#l2={2,{2,3,4},5,6,7} #not set
#print(l1)
#print(l2)
#print(l3)
#converting list to a set
m=[99,6,7,33]
m1=set(m) #converting list to set
print(type(m1))
print(type(m))
#union
n1={9,5,6,1}
n2={1,3,2,5}
print(n1.union(n2)) # ALL elements with no duplicates
print(n1|n2) # both perform the same operation
#intersection
print(n1.intersection(n2)) #Only common elements
print(n1&n2) # both perform the same operation
#difference
print(n1.difference(n2)) #except common elements from one set
print(n1-n2) #9,6
print(n2-n1) #2,3
#symmetric_difference
print(n1.symmetric_difference(n2)) #except the common elements
print(n1^n2)
print(n2.symmetric_difference(n1))
#min max and sum
o={1,2,3}
print(min(o))
print(max(o))
print(sum(o))


