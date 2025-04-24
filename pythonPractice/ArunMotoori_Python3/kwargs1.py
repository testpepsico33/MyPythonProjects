
def sample(**kwargs):
    for k, v in kwargs.items():  # iteam refers to both key and value, k,v iterating double values
        print(k,v)

sample(name="Nirmal", experience=6, location="Bangalore")

def demo(name, experience, location):
    print(name, experience, location)

d={"name":"Nirmal","experience":6,"location":"Bangalore"} #using dictionary assigning arguments to the function parameters

demo(**d)