
name="Nirmal Kumar"
experience= 6.6
location="Bangalore"

print("My name is "+name+" I have around" +str(experience)+ "years of expereince and I stay in "+location)

print("My name is "+name+" I have around",experience,"years of expereince and I stay in "+location)

print("My name is {} I have around {} years of expereince and I stay in {}".format(name,experience,location))

print("My name is {1} I have around {2} years of expereince and I stay in {0}".format(location,name,experience))

print("My name is %s I have around %d years of expereince and I stay in %s"%(name,experience,location))

print("My name is %s I have around %f years of expereince and I stay in %s"%(name,experience,location))
