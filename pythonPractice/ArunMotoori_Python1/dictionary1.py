#creating dictionary with indentation
car={
    "brand":"honda",
    "model":"amaze",
    "milage":"14.5",
    "price":950000}
print(car)
print(type(car))
#get values of key
print(car.get("model")) #syntax1 "dictionary_name.get(key)"
print(car["price"]) #syntax2 "dictionary_name[key]
#printing all keys of the dictionary
print(car.keys()) #syntax3 "dictionary_name.keys
#printing all values of the dictionary
print(car.values()) #syntax4 "dictionary_name.values
#updating the values of the dictionary
print(car["price"]) #before update
car["price"]=7500000
print(car["price"]) #after update
#adding new key value to the existing dixtionary
print(car) #before update
car["type"]="hatchback"
print(car) #before update
#using for each loop in dictionary
for v in car.values():
    print(v)
    #print(car[k])
for k in car.keys():
    print(k,car[k]) #gives both key and values
for k in car:
    print(k)
#iterating both key and values using "k,v"
for k,v in car.items(): #items function fetch the both key and values
    print(k,v)
#pop
print(car) #befor pop
car.pop("type")
del car["price"] #pop and del can help to delete both key and values
print(car) #after pop
#removing the last value of the dictionary
car["price"]=650000
car["type"]="hatchback"
print(car) #befor popitem
car.popitem() #last iteam will be removed
print(car) #after popitem
#removing all the k v iteams
print(car)
car.clear()
print(car)
car={
    "brand":"honda",
    "model":"amaze",
    "milage":"14.5",
    "price":950000}
#len
print(len(car))
#deleting entire dict
#del car
print(car)
#comparing 1 dictionary with another
car1={
    "brand":"honda",
    "model":"amaze",
    "milage":"14.5",
    "price":950000}
car2={
    "brand":"honda",
    "model":"amaze",
    "milage":"14.5",
    "price":950000}
car3={
    "brand":"honda",
    "model":"amaze",
    "price":950000}

print(car1==car2)
print(car1==car3) #in car3 removed 1 key and value pair
print(car1!=car3)

#order of key value pair dosent matter
