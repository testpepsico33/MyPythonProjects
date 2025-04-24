
#Prime number program 1 to 100

for i in range(1,101):
    for j in range(2,i):
        if i%j ==0:
            break
    else:
        print(i)

print(6%2)

#Prime or Not
num= int(input("Enter the Number: "))
count =0
for i in range(1,num+1): #(1,3) ->1,2
    if num% i==0: #1%1 ==0; 2%1 ==0
        count+=1 # count=1, count=2
if count == 2: # count 2; 2==2
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
