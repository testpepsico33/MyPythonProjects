#As python not supporting overloading we can use the below alternetway to achive
class A:

    def sample(self,a=None,b=None):
        if a!=None and b!=None:
            print(a*b)
        elif a!=None:
            print(a)
        else:
            print("Nothing")

obj=A()
obj.sample(5,4)
obj.sample(5)
obj.sample()

class SampleA:
    def sample(self):
        print("A")
    def sample(self,a,b):
        print("B")

obj2=SampleA()
obj2.sample()
