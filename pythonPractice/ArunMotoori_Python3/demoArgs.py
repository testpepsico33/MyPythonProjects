

def sample(*args):
    for i in args:
        print(i)

sample(1,2,3,4,5,6,7,8,9)

def sample1(a,b,c,d,e):
    for i in args:
        print(i)
args=[2,3,9,6,5]
sample1(*args)

def keyvalue(**kwargs):

    for k,v in kwargs.items():
        print(k,v)

keyvalue(name='Nirmal',age="34",profession="AI/ML scientists")

def keyvalue(name,age,profession):
    print(name,age,profession)

d={"name":"Nirmal","age":34,"profession":"AI/ML scientists"}

keyvalue(**d)
