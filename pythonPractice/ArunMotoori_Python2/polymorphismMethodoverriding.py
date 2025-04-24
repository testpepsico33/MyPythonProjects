#Properties in the child class and properties in the parent class matches. parent class properties overriddent by child class properties
class A:
    a=5
    def sample(self):
        print("Inside sample method of class A")
class B(A):
    a=10
    def sample(self):
        print("Inside sample method of class B")

obj=B()
obj.sample()
print(obj.a)