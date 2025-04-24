def my_first_function():
    print("This is my first function")

my_first_function() #Function calling

def print_name(name): #parameter
    print("your name is:"+name)
print_name("Nirmal Kumar") #First function calling argument
print_name("Nandhini") #Second function calling argument
print_name("Arav") #Third function calling argument

def print_name(name="Kavin"): #passing default argument
    print("The name is:"+name)

print_name()     #argument is not passed so default argument is called
print_name("Aravin") #argument is passed default argument is not called

#Function with multiple argument

def sum(a,b,c,d):
    print(a+b+c+d)
sum(1,2,3,4)

#Function returning data

def sum(a,b): #parameter a,b
    return a+b
c=sum(1,2)
print(sum(1,2))
print(c)

def add(a,b):
    c=a+b
    d=a-b
    print(c)
    print(d)

add(10,20)

#Multiple Functions can be created
def sum(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

sum(5,4)
sub(5,4)
mul(5,4)
div(5,4)

#collecting inputs from user

print("Enter the a value")
num1=input()
print("Enter the b value")
num2=input()

total=str((int(num1)*int(num2)))
print("Multiplication of 2 number:"+total)

#max() and min() in-built functions in python
max_num=max(1,2,3,4,5,10000,6)

print(max_num)

min_num=min(1,2,3,4,5,10000,6)

print(min_num)

min_alph=min("Orange","Apple","grapes")

print(min_alph)

max_alph=max("Orange","Apple","grapes")

print(max_alph)