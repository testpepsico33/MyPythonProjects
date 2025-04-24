
class A:

    _age=0

    def set_age(self,age):
        A._age=age
    def get_age(self):  
        return A._age

obj=A()
obj.set_age("33")
print(obj.get_age())
