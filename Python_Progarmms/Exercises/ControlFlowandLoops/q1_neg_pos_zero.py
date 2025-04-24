

def check_number(number):
    if number>0:
        return "Positve"
    elif number<0:
        return "Negative"
    else:
        return "Zero"

num=float(input("Enter the number"))
result=check_number(num)
print(result)

#print("Enter the number")
#number=int(input())