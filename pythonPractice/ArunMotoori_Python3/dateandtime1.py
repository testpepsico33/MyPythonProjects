import datetime

d=datetime.datetime.now()
print(d) #Ouptput: 1990-06-07 17:41:33
print(d.time())
print(d.date())
print(d.hour)
print(d.min)
print(d.second)
print(d.year)
print(d.strftime("%dth %B  %Y" )) #7th June 1990 Go to datetime format url-->https://www.w3schools.com/python/gloss_python_date_format_codes.asp
print(d.microsecond)