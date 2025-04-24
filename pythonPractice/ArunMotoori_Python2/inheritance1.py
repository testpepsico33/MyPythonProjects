
class A:
    a=10

    def method_a(self):
        print("Inside Method A")

class B(A): #Inheriting from child class to parent class(Single inheritance (B inherites A))
    b=20

    def method_b(self):
        print("Inside Method B")
class C(B): #Multilevel inheritance(C inherites B inherites A)
    c=30

    def method_c(self):
        print("Inside Method C")
#Below is the Hieratchical inheritance both class D and E inherites class A
class D(A):
    d=40
    def method_d(self):
        print("Inside Method D")
class E(A):
    e=50
    def method_e(self):
        print("Inside Method E")
#Below is the multiple inheritance class F(A,B):
class F(A,B):
    f=50
    def method_f(self):
        print("Inside Method F")
#Hybride-Hierichical+multiple
class G(A,E):
    g=60
    def method_g(self):
        print("Inside Method G")
obj=C()
#Object created for child class along after inheriting it we can access the child class and parent class as well
obj.a
obj.b
obj.c
obj.method_a()
obj.method_b()
obj.method_C()


