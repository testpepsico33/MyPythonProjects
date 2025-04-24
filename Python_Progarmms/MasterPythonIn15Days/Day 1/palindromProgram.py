def is_simple_palindrome(text):
    processed_text = "".join(text.lower().split())  # text converts to lower case and spliting it and join and store ina variable

    return processed_text == processed_text[::-1]


input_string = input("Enter a string: ")

if is_simple_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")


def palindrom(text):
    text_processing = "".join(text.lower().split())
    return text_processing == text_processing[::-1]


input_string1 = input("Enter a string:")

if palindrom(input_string1):
    print(f" palindrom")
else:
    print(f"Not a palindrom")
