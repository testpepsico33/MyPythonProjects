#printing list
a=[6,9,3,1,5]
print(a)

#indexing -- Accessing specific value using indexing concept
print(a[3])
print(a[0])

#Size of the list
print("Size of the list is:"+str(len(a))) #Using "len" function we can find the size of the list

#List using in "for loop" with range function
for i in range(len(a)):
    print(i) #printing the index values

    print(a[i]) #printing the a values

#List using "for each loop"
for e in a:# for each and every element in the list is printed
    print(e)

#updating elements in the list
b=[6,9,3,2]
print(b) #before update
b[3]=7
print(b) #after update

#Appending the elements to the end of the list using append()
appending=[4,5,6,9]
print(appending) #before append
appending.append(33)
print(appending) #after append

#inserting element in between the list
inserting=[5,9,6,4,1]
print(inserting) #before insert
inserting.insert(4,2)
print(inserting) #after insert

#removing element in from the list
removing=[9,7,999,6,5]
print(removing) #before remove
removing.remove(999)
print(removing) #after remove

#removing last element from the element using pop
popfunction=[33,44,55,66,18]
print(popfunction) #before pop
popfunction.pop()
print(popfunction) #after pop

#pop indexing
popindexing=[22,11,18,33,55,66]
print(popindexing) #before pop index
print(popindexing.pop(2)) #print the removed value and #when dont want to remove the last element of the list wants to remove the particular element of the list
print(popindexing) #after pop index

#Empty the list not deleting the list
clearlist=[1,2,3,4,5]
print(clearlist) #before clear
clearlist.clear()
print(clearlist) #after clear

#reverse the list
reverselists=[3,6,9,12,15]
print(reverselists) #before reverse
reverselists.reverse()
print(reverselists) #after reverse

#sort the list
sortalphabets=["orange","green","yellow","blue","white"]
print(sortalphabets) #before sort
sortalphabets.sort() #sorted in ascending order
print(sortalphabets) #after sort

#index inbuild function
index_inbuild_function=[9,3,5,7]
print(index_inbuild_function.index(7)) #gives the elements index value

#Nested list
nestedlist=[6,[3,5,6,9],9,3,5]
print(nestedlist[1])
print(nestedlist[1][2]) # this will give the inner list index value

#Can store different types of values in same list
differentvalues=["Mahindra","XUV 7oo",15.5,2500000]
print(differentvalues[2])
print(differentvalues[0])

#backwordindex and forwardindex
indexing=[2,3,5,6]
print(indexing[1]) #Forward index
print(indexing[-2]) # -2+4=2 Backword index
print(indexing[-3]) # -3+4=1 Backword index
print(len(indexing))

#Slicing List
slicing=[9,1,5,7,6]
print(slicing[1:4]) # index : position
print(slicing[:3]) #0 index  : position
print(slicing[1:]) #index : last position
print(slicing[:]) #0 index : last position

s="nirmal"
print(s[::-1])

#Finding the number of times the element is repeated in the list using count()
repeatedelements=[9,1,2,5,6,9,9,6,6,6,6,5]
print(repeatedelements.count(9))
print(repeatedelements.count(6))
print(repeatedelements.count(5))

#max and min value in the list
value=[9,1,2,5,6,9,9,6,6,6,6,5]
print(max(value))
print(min(value))

#sum of element in the list using sum()
elements=[1,2,3]
print(sum(elements))
print(type(elements)) # type gives us the data type of the variable

#deleting the list
aa=[9,8,7,6,5,1]
print(aa) #before delete
del(aa)
#print(aa) #after delete

#using "in" and "not in" operator using list
b=[2,7,5,9]
print(9  in b) #True
print(15 in b) #False
print(19 not in b) #True

#Concatenating two list using +operator
list1=[1,3,5,7,9]
list2=[2,4,6,]
list3=list1+list2
print(list3)

#Extending the list
A=[1,2,3,4,5]
B=[6,7]
A.extend(B)
print(A)
