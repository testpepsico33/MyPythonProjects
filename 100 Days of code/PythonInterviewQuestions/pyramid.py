def calculate_pyramid_values(name):
    """
    Calculates the pyramid values based on the given name.
    """
    name = name.lower()
    letter_values = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 8, 'g': 3, 'h': 5,
        'i': 1, 'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 7, 'p': 8,
        'q': 1, 'r': 2, 's': 3, 't': 4, 'u': 6, 'v': 6, 'w': 6, 'x': 5,
        'y': 1, 'z': 7
    }

    total = 0
    for char in name:
        if 'a' <= char <= 'z':
            total += letter_values[char]

    pyramid = [total]
    pyramid_rows = [str(total)]

    while pyramid[0] > 9:
        digits = [int(d) for d in str(pyramid[0])]
        pyramid[0] = sum(digits)
        pyramid_rows.append(str(pyramid[0]))

    return pyramid_rows

def print_pyramid(name):
    """
    Prints the pyramid output based on the calculated values.
    """
    pyramid_rows = calculate_pyramid_values(name)
    if len(pyramid_rows) > 1:
      first_row = ""
      for digit in str(int(pyramid_rows[0])):
        first_row = first_row + digit
      print(first_row)

      working_row = int(pyramid_rows[0])

      while working_row > 9:
        working_row_string = str(working_row)
        new_row = ""
        for i in range(len(working_row_string)-1):
          new_digit = int(working_row_string[i]) + int(working_row_string[i+1])
          if new_digit > 9:
            new_digit = sum([int(d) for d in str(new_digit)])
          new_row = new_row + str(new_digit)
        print(new_row)
        working_row = int(new_row)

# Example usage:
name = "nirmal kumar"
print_pyramid(name)

name = "test name"
print_pyramid(name)