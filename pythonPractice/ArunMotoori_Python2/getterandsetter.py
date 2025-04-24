
class A:
    __age=0

    def set_age(self,age):
        A.__age =age #setting value 
    def get_age(self):
        return A.__age

obj=A()
obj.set_age("33")
print(obj.get_age())