
def common_letter():
    string1=input("Enter the first string:")
    string2=input("Enter the second string:")
    s1=set(string1)
    s2=set(string2)
    print(s1)
    print(s2)
    Final_set=s1&s2 # when 2 set intersecting returns the common values
    print(Final_set)
    print(type(Final_set))
common_letter()