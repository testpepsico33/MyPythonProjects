
def swap_the_value(a,b):
    temp = a
    a = b
    b = temp
    return a,b

x= 10
y= 20

print("Before swap",x,y)
"""
result= swap_the_value(x,y)

print("After swap",result)
"""
x,y=swap_the_value(x,y)
print("After swap",x,y)

