
class Car:
    wheels=4
    def start_car(self):
        print("Car Started")

    def sample(self,brand,model,price,milage):
        # brand,model,price,milage outside the method how to do?
        #To convert method variable to class variable we have to assign as "self.brand=brand"
        self.brand=brand #converted to class level variable from method variable
        self.model=model #converted to class level variable
        self.price=price #converted to class level variable
        self.milage=milage #converted to class level variable
        print(brand,model,price,milage)
    def sample_two(self):
        #In this class we have 5 class level variables those are wheels(assigned directly in class level),brand,price,milage,model(Assigned in method level and converted as class variable)
        print(self.wheels,self.brand,self.milage,self.price)
    def sample_three(self):
        print(self.wheels)
        self.start_car()


car1=Car()
car1.sample("Honada","Amaze","9000000","14.5")
car1.sample_two()
car1.sample_three()