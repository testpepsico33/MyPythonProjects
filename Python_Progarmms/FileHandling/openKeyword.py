#Here no need to give close with is executed automatically file is closed
with open("file","r") as file:
    content=file.read()
    print(content)