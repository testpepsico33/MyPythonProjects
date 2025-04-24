
list1=[2,6,5,7,9]
list2=[3,4,5,9,6]

res_lst= []

for i in range(0,len(list1)):
    res_lst.append(list1[i]+list2[i])
# iteration1 ->list1[0]+list2[0] ->2+3 =5
# iteration2 ->list1[1]+list2[1] ->6+4 =10
# iteration3 ->list1[2]+list2[2] ->5+5 =10
# iteration4 ->list1[3]+list2[3] ->7+9 =16
# iteration5 ->list1[4]+list2[4] ->9+6 =15
print(res_lst)