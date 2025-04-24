

s="madam"

print(s[::-1])

if s==s[::-1]:
    print("it is palindrom")
else:
    print("it is not a palindrom")


def is_palindrome(string):
    reverse_string=string[::-1]
    return string == reverse_string

word= "madam"

if is_palindrome(word):
    print(f"{word} is a palindrom")
else:
    print(f"{word} is not a palindrom")








