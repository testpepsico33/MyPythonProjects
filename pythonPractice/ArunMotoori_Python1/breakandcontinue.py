for i in range(1,10):

    if i==5:
        continue
    print(i)

print("printing next program")

for i in range(1,10):

    if i==5:
        break
    print(i)

print("Printing whileloop program")

i=1
while i<=10:
    if i==5:
        i = i + 1
        break
    print(i)
    i = i + 1