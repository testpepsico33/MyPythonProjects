
class A:
    a=5
    def sample(self):
        print("inside class A sample method")
class B(A):

    a=10
    def sample(self):
        print("inside class B sample method")
    def print_properties(self):
        print(super().a)
        super().sample()
        print(self.a)
        self.sample()

obj1=B()
obj1.print_properties()

class C:
    def __init__(self):
        print("Inside __init__ method of class C")
class D(C):
    def __init__(self):
        super().__init__()
        print("Inside __init__ method of class D")

obj2=D()
