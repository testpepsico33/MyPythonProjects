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
