def cal_fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * cal_fact(n - 1) #3,2,1


num = int(input("Enter a number: "))
factorial = cal_fact(num)
print(f"The factorial of {num} is {factorial}.")
