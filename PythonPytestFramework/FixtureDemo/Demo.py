
def count_line():
    file= open("C:\\Users\\nimalkumar.j\\PycharmProjects\\PythonPytestFramework\\Files\\Text_file.txt","r")
    read_file= file.readlines()
    print(read_file)
    file.close()


string1="word1"
string_replace=""
def reverse():
    string1 = "word1"
    for i in range(string1):
        if i == "a,e,i,o,u":
            string_replace="*"


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function.")
        func()
        print("Something is happening after the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


