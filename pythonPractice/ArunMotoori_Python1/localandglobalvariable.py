
def my_functionLocal():
    name="Local Variable"
    print(name) #Local variable initialized inside the function
my_functionLocal()
#print(name)    #local variable cant call from outside the function

name="Global Variable" #Global Variable
def my_functionGlobal():
    print(name)
my_functionGlobal()
print(name) #Global variable can be called within the python file both inside and outside the function

#Global Keyword
company="infosys"
def global_keyword():
    global company #Using global key word we can access the variable both inside and outside the function
    company ="google" #Global variable key chnage the behaviour of local variable to gloable variable
global_keyword()
print(company)
