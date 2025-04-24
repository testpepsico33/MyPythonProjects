"""
Task
Given an integer, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
"""
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n>20:
        print("Not Weird")

# n=[0,1,2,3] output= 0,1,4,9
n = int(input())

for i in range(n):
    square = i * i
    print(square)

#leap year or not

def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    # This 'else' block is executed if the year is divisible by 4
    # BUT NOT divisible by 100.
    # According to the rules, such a year IS a leap year.
    return leap


year = int(input())
print(is_leap(year))

