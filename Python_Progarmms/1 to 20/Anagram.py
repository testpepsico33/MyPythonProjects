str1="listen"
str2="silent"

str1=str1.replace(" ","").upper()
print(str1)

str2=str2.replace("","").upper()
print(str2)

if sorted(str1) == sorted(str2):
    print(str1)
    print(str2)
    print("True")
else:
    print("False")

str3='a','b','c','d','e','3','6','9'
print(sorted(str3))
type(sorted(str3))

#Counting white space
string=" p r o g ram"
print(string.count(" "))

#palindrom

string="kayak".lower()

if string == string[::-1]:
    print("True")
else:
    print("False")