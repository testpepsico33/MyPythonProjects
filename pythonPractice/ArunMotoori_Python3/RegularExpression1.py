import re
#patter= "Nirmal"
#pattern ="[Pp]ython" #If user input is Python. Pattern does not match. To fix this give "[Pp]ython"
#pattern ="ye[sp]" # Last value can be any of [sp]
#pattern ="[skf]it"# First value can be any of [skf]
#pattern ="[9157]it" # First value can be any of [9157]
#pattern ="[A-Z]it" # First value can be between A to Z and should be in capital letter
#pattern ="[0-9]it" #Fist value can be between 0 to 9
#pattern ="[4-9]it" #Fist value can be between 4 to 9, will give error if choose 0 to 3
#pattern ="[a-zA-Z0-9]it" #trying all combination together
#pattern ="[^0-9]it" #Apart from 0 to 9 the pattern did not match. The First character should not be a number will accept both Capital ans small letter
#pattern ="se[a-z]" # Last value can be between a to z small letter
#pattern ="se[^aeiou]t" #cap between text cant be a vowels
#pattern ="s\dt" #\d means o to 9 numbers the middle character should be a number
#pattern ="s\Dt" #\D is equal to [^0-9] , the middle value should not be a number
#pattern ="s\wt" #\w equal to specifying [A-Za-z0-9] will not accept
#pattern ="s\Wt" #\W equal to specifying [^A-Za-z0-9] will accept only symboles example #,$.% etc
#pattern ="^My" #Text starting letter should be My
#pattern ="Nirmal$" #Text ending with should be Nirmal
#pattern ="A..n" #Single dot reperesent single character that can be any
#pattern ="^My.*Nirmal$" #.* any number of chaaracter , ^My -start with My, Nirmal$-End with Nirmal. MyNirmal is accpetd
#pattern ="^My.+Nirmal$" #.+ minimum one character should be present. MyNirmal is not accpetd
#pattern ="^My.?Nirmal$" #.? 0 or 1 time is accepted Ex:My Nirmal and MyNirmal accepted, Not accepted My name is Nirmal
#pattern ="^My.{2}Nirmal" #.{2} the expression should be repeated twice
#pattern ="python|Python" #Any one word should be match
pattern ="[A-Z]ython|[a-z]ython" #Fist letter can be both capital and small letter
print("Enter your input here:")
text=input()

if re.search(pattern,text): #re.serach function return true the input value matches with pattern value
    print("Patter got matched")
else:
    print("Patter did not matched")
