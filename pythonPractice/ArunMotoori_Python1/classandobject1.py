#The function which is created outside the class is called "FUNCTION"
def sample_fun():
    print("Inside sample templet")

a=9
#Created class template/Blueprint
class car:
    wheel=4
    #The function which is created inside the class is called "METHOD"
    def start_car(self):
        print("Car started")
#The below is the object creation statement
hamaze=car() # hamaze9 is "OBJECT REFERENCE" not variable ; car() is a "OBJECT"
sample_fun()
print(hamaze.wheel)
print(a)
hamaze.start_car()

#Creating another object reference for car() class
svdi=car()
print(svdi.wheel)
svdi.start_car()

