

class car:
    wheel = 10

    def __init__(self,brand,model,mileage):
        self.brand=brand
        self.model=model
        self.mileage=mileage
    def Car_details(self):
        print("Car details" +self.brand+" "+self.model+" "+self.mileage) # Accessing method variable by implementing self
        #self.method_static() #Accessing static method from instance method
    @staticmethod
    def method_static():
        print("Static method")
        c1=car("Hyundai","i10","66")
        c1.Car_details() #accessing instance method from static method by creating object






c1=car("TATA","NEXON","33")
print(c1.brand)
c1.Car_details()
car.method_static()
