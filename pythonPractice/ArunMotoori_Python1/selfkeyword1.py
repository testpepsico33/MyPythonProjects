
class Car:

    wheels=4

    def start_car(self):
        print("Car Started")
    def example_one(self):
        print(self.wheels) #Using "self keyword" to access the class properties inside the class
        self.start_car()
#using "object reference" we can access the class properties of the class outside the class
honda=Car()
print(honda.wheels)
honda.start_car()
honda.example_one()
