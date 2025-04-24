
numberList=[12,3,55,33,6,23,77,4]

max=numberList[0]

for num in numberList:
    if max < num: #The program checks if the current value of max is less than the current element (num).
#max (12) < num (55) is true. Untill next condition satisfies 55 remains maximum value
        max = num
print(max)

#converting a list into a string
list=['n','i','r','m','a','l']

string="".join(list)
print(string)


