#the moment we creat an iter() for a collection . the pointer is pointing outside to the list
#Once the next function is created the pointer pointing to the first value of the list
#List using in iter()
a=[9,1,2,4,5]
itr=iter(a)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

#Tuple using in iter()
a=(9,1,2,4,5)
itr=iter(a)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

#Set using in iter()
a={9,1,2,4,5}
itr=iter(a)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

#Dict using in iter()
a={"Name":"Nirmal","age":33,"Location":"Bangalore","State":"Karnataka","Pincode": 560100}
itr=iter(a.items())
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
