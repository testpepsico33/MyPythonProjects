
class Car:
    def initialization_method(self,brand,model,price,milage):
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

svdi=Car() #svdi is a 1st Object reference created for the object Car()
svdi.initialization_method("Maruthi","Swift","80000001","24") #initializing data

hamz=Car() #hamz is a 2nd Object reference created for the object Car()
hamz.initialization_method("Honda","Amaze","9000000","14.5") #initializing data

svdi.car_start()
svdi.car_stop()
svdi.print_car_details()

hamz.car_start()
hamz.car_stop()
hamz.print_car_details()
