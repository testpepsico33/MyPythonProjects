n = int(input())
for i in range(1,n+1):
    print(i, end='')
    print()

print("Hello", end='')
print("World")
# end='' is specified, no newline character is added at the end.
# The cursor remains at the end of "Hello".