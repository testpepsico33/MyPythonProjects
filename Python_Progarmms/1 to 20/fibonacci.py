
fib=[0,1]

n=5
for i in range(n):
#fib[-1] refers to the last element in the list.

#fib[-2] refers to the second-to-last element in the list.
   fib.append(fib[-1]+fib[-2])
# fib=[0,1] -->length 2 ; fib[-1] --> -1 -> 2-1=1 ->fib=[0,1]= value 1; fib[-1]=1; fib[-2]=2-2=0

# fib=[0,1,1,2,3,5,8]
# converting the int list to list str
# ','.join(str(e) -> adding "," and joining the str
print(','.join(str(e) for e in fib))




