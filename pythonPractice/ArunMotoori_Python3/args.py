
def sample(*args): #instead of args we can assign other variable names as well
    print(args)
    for i in args:
        print(i)

sample(9,1,2,6,7,5) #for single parameter passing multiple arguments that is the advantage of *args


def function(a,b,c,d):
    print(a,b,c,d)

args=[1,2,3,4]
function(*args) #instead of sending multiple arguments directly via function we can create a list as args and we can send as *args


