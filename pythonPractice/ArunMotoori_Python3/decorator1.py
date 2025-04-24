def my_decorator(func):
    def inner_method():
        print("Thanks for choosing Arav Technologies")
        func()
        print("Keep growing with us")
    return inner_method

@my_decorator
def aravtechnology():
    print("Welcome to the Arav Technologies")
aravtechnology()