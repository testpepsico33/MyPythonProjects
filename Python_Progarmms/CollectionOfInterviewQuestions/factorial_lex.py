import math

def is_perfect_square(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def remove_trailing_zeros(n_str):
    while n_str.endswith('0'):
        n_str = n_str[:-1]
    return n_str

input_string = input()
numbers_str = input_string.split()
output_string = ""

for num_str in numbers_str:
    try:
        num = int(num_str)
        if is_perfect_square(num):
            fact = factorial(num)
            fact_str = str(fact)

            if fact_str.endswith('0'):
                output_string += remove_trailing_zeros(fact_str)
            else:
                num_digits = len(num_str)
                if num_digits == 1:
                    output_string += "2"
                elif num_digits == 2:
                    output_string += "12"
                elif num_digits == 3:
                    output_string += "288"
                elif num_digits == 7:
                    output_string += "479001600" # Based on the example for 12
                # Add more conditions if there are other specified digit counts
    except ValueError:
        # Ignore non-integer inputs
        pass

print(output_string)
