#wrapping up in a "UNIT" which means class
class A:
#to achive encapsulation we are setting up the private variable
    __age=0 #private variable-->DATA
#to access and modify the private variable we use getter and setter method
#This non private variable called "CODE"
    def get_age(self,age):
        A.__age=age
    def set_age(self):
        return A.__age

obj=A()
obj.get_age(33)
print(obj.set_age())
#this is how the encapsulation is achived