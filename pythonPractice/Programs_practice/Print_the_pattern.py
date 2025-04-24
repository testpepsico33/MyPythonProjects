row=5
for i in range(1,row+1,1):
    for j in range(1,i+1):
        print(j,end='') #end='' To print next iteration in same line
    print("") #-next line

    #for j in range(1,1+1):
    # --> i=1 ->1
    #for j in range(1,2+1):
    # --> i=2 ->12
    #for j in range(1,3+1):
    # --> i=3 ->123
    # for j in range(1,4+1):
    # --> i=4 ->1234
    ## for j in range(1,4+1):
    # --> i=5 ->12345