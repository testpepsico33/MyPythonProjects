class A:
    __a=33 #Private Variable
    def __sample(self): #Private Method
        print("sample method")
    def print_details(self): # Accessing private variable and method with the help of non private method
        print(self.__a)
        self.__sample()
obj=A()
obj.print_details() #Directly not able to access the private properties outside the class using seperate method we can access them
