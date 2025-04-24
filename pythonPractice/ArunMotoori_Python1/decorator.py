

def sum(a,b):
    print(a-b)
def sub_b(func):

    def inner_sum(a,b):
        if a>b:
            a,b==b,a
            return sum(a,b)

    return inner_sum()

sum1=sub_b(sum)
sum1(9,2)
