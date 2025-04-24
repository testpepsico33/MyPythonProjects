
word =input("Enter the String:")
num=0
for i in word:
    num += 1
print(num)

#Count the positive and negative values in a list
number_list=[1,2,3,4,-1,2,-3,4,-5]
positive_number=0
negative_number=0
for i in number_list:
    if i >= 0:
        positive_number += 1
    if i <= 0:
        negative_number += 1
print(positive_number)
print(negative_number)