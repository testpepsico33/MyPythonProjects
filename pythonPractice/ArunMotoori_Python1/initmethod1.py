

class Car:
    def __init__(self,brand,model,price,milage):
        self.brand=brand
        self.model=model
        self.price=price
        self.milage=milage

    def car_start(self):
        print(self.brand+" car having model as "+self.model+"has started")

    def car_stop(self):
        print(self.brand+" car having model as "+self.model+"has stopped")

    def print_car_details(self):
        print("Brand of the car is :"+self.brand)
        print("Model of the car is :"+self.model)
        print("price of the car is :"+str(self.price))
        print("Milage of the car is :"+str(self.milage))
        print("----------------------------------------")

svdi=Car("Maruthi","Swift","80000001","24") #Values assigned within the object that will send to init method
#no need of extra code. If its was intialized in normal method need to write extra code to initialize the value

hamz=Car("Honda","Amaze","9000000","14.5")


svdi.car_start()
svdi.car_stop()
svdi.print_car_details()

hamz.car_start()
hamz.car_stop()
hamz.print_car_details()
