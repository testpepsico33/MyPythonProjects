from abc import ABC, abstractmethod
class A(ABC):

    def __init__(self,a):
        self.a=a

    @abstractmethod
    def method_one(self):
        pass
    @abstractmethod
    def method_two(self):
        pass
    def method_three(self):
        print("Inside method_three",self.a)
class B(A):
    def method_one(self):
        print("Inside the method one")
class C(B):
    age = 33
    def method_two(self):
        print("Inside the method two")
c=C(33)
c.method_one()
c.method_two()
c.method_three()
print(c.age)
