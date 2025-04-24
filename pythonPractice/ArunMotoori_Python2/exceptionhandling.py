
print("Staring of the program 1")
try: #exception handled using try block if not error will be appeared rest og the code not executed
    a=10/1
except ZeroDivisionError as z:
    print("Exception Handle :",z)
else:
    print("Inside else block")
finally:
    print("inside finally block")

#NameError
print("starting of the program 2")

try:
    print(a)
except NameError as n: #n will describe about the exception, in this case "name a is not defined"
    print("Exception got handled : ",n)

print("ending of the program 2")

#Manually raising exception

print("staring of the program 3")

#raise ZeroDivisionError

print("ending of the program 3")

print("start of the program 4")
print("Input your child age")
age= int(input())
try:
    if age<5:
        raise ValueError("Below 5 years of age not eligble")
    else:
        print("Your Child is eligible")
except ValueError as v:
    print("Exception handled: ",v)