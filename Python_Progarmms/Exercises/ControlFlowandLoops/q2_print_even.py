
def check_even(number):
    count = 0
    for num in range(1,21):

        if (num % 2 ) == 0:
            print(num)
            count=count+1
num=int(input("Enter the number"))
result=check_even(num)
print(result)