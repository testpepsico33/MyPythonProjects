print("1", end=" ") #end is a keyword used to print the statement in same line
print("2", end=" ")
print("3", end=" ")


a= 10
a= "Arav"
a= True

print(a)

p,q,r=1,2,3
print(p,q,r)

p=q=r=3
print(p,q,r)

#snack case --> Lower case with _ is called snack case
my_fisrt_name="Nirmal"
my_last_name="Kumar"

a=6 # initilizing
a=10 # updating

print("The value stored in the variable in the a is:", a)

#type casting

#Before type casting
a="9"
print(type(a))
print(a)

#After type casting
a=int("9") #string value 9 is converted to int
print(type(a))
print(a+1)

a=float(9)
print(type(a))
print(a)
print(a+1.1)

a=float("9") #Converting string to float
print(type(a))

a=str(9.1) #Converting float to string
print(type(a))
print(a+" is a string number")

#Complex data type
c= 3+5j
d= 4+5j
print(c)
print(type(c))
print(c.real)
print(c.imag)
print(c+d)
print(c*d)
e= 3j
print(e.real)
print(e.imag)

#Range data type

r=range(3) #0,1,2
print(r) #o/p- range(0, 3) 0- start value ; 3 - number of values
print(type(r))

for v in r:
    print(v)

r=range(1,5) #1,2,3,4 ; to conut number of values 5-1 =4

for v in r:
    print(v)

r=range(2,7) #2,3,4,5,6 ; to conut number of values 7-2 =5

for v in r:
    print(v)

#Sequcing in Ascending order
r=range(1,11,1) #Sequencing 1 value 1,2,3,4,5....10
r=range(1,11,2) #Sequencing 2 value 1,3,5,7,9
r=range(1,11,3) #Sequencing 3 value 1,4,7,10
for v in r:
    print(v)

#Sequcing in Descending order
r=range(10,0,-1) #Sequencing -1 value 10,9,8,7,6,5,4,3,2,1
r=range(10,0,-2) #Sequencing -2 value 10,8,6,4,2
for v in  r:
    print(v)

#Range with indexing
r=range(10,15) #10,11,12,13,14
print(r[0]) #10
print(r[2]) #12

#Slicing

r=range(12,18) #12,13,14,15,16,17
s=r[1:4] # 1 is a index value : 4 is a position
for v in s:
    print(v)
