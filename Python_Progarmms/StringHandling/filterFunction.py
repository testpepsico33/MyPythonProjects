
def is_even(n):
    return n%2==0

num=[1,2,3,4,5,6]

even_number=filter(is_even,num)
print(list(even_number))