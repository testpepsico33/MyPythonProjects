#Use object reference for instance variable. Instance varaiables are uncommon which is changeable
#Use class reference for static variable. Static variable is common which is not changeable

class Car:
    wheels=4 #static variable


    def __init__(self,brand,model,price,milage):
        self.brand=brand
        self.model=model
        self.price=price
        self.milage=milage

    # Instance method can access both the static and instance stuffs
    def start_car(self):
        print(self.brand+" car having as "+self.model+" has started")
        Car.demo_satmethod() #demo method belongs to static method as discussed we can access both static and instance stuffs

    # Creating static methods
    # important:Static method can access only the static stuffs
    @staticmethod
    def demo_satmethod():
        print("demo static method")

    @staticmethod
    def print_car_wheel(): #Self keyword not supported in static method
        print(Car.wheels)
        Car.demo_satmethod()
        #Still we can access the instance method inside the static class by creating object and use it, below is the example
        c1=Car("Hyundai","i20",10000000,13)
        print(c1.brand)
        c1.start_car()


svdi=Car("Maruthi","Swift VDI",7500000,24)
hamz=Car("Honda","Amaze",9000000,15.5)
svdi.start_car()
Car.print_car_wheel()
Car.demo_satmethod()
print(svdi.wheels)
print(Car.wheels)


