from abc import ABC, abstractmethod

class AbstractClass(ABC):

    @abstractmethod
    def methodOne(self):
        pass
    @abstractmethod
    def methodTwo(self):
        pass
    def methodThree(self):
        print("Inside non abstract methodThree ")
    @abstractmethod
    def methodFour(self):
        pass

class instantiateAbstract1(AbstractClass):

    def methodOne(self):
        print("inside abstract methodOne")
    def methodTwo(self):
        print("inside abstract methodTwo")

class instantiateAbstract2(instantiateAbstract1):
    def methodFour(self):
        print("Inside abstract methodFour")
obj=instantiateAbstract2()
obj.methodThree()
obj.methodOne()
obj.methodTwo()
obj.methodFour()