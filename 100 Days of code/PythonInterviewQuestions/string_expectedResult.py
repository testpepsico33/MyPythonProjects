str="india"

print(str[-1])
print(str[:-1])
print(str[::-1])

list1=['my','name']
list2=['is','Arav']
list3=list1+list2
print(list3)

list1.extend(list2)
print(list1)

print(' '.join(list1))
print(type(list1))

#combine 2 list and convert it to a dictionary as shown below

list1=['a','b','c']
list2=[1,2,3]
x=zip(list1)
print(list(x))

dict1=dict(zip(list1,list2))
print(dict1)


list6=[1,2,3]
list7=['a,','b','c']
x=dict(zip(list6,list7))
print(x)

dict3=  { list6[i]: list7[i] for i in range((len(list6)))}
print(dict3)

dict4={}

for key in list6:
    for value in list7:
        dict4[key]=value
        list7.remove(value)
        break
print(dict4)