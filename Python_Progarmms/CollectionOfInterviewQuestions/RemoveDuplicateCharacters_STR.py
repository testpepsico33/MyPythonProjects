#Approach 1
#input_string="mississippi"
input_string="csharpcorner"
result=""

for char in input_string:
    if char not in result:
        result=result+char
print(result)

#Approach 2
def remove_duplicate_characters(input_string):
  """Removes duplicate characters from a string while preserving the order
  of the first occurrence.

  Args:
    input_string: The input string.

  Returns:
    A new string with duplicate characters removed.
  """
  seen_characters = set() #Empty set assign it to the variable seen_character
  result = ""
  for char in input_string:
    if char not in seen_characters:
      seen_characters.add(char)
      result += char
  return result

# Get input from the user
input_str = input("Enter a string: ")

# Remove duplicate characters
output_str = remove_duplicate_characters(input_str)

# Print the output
print("Output =", output_str)

#Approach 3

def remove_duplicates_loop(input_string):
  """Removes duplicate characters from a string while preserving the original order
  of the first occurrence of each character using a loop and a new string.

  Args:
    input_string: The input string.

  Returns:
    A new string with duplicate characters removed.
  """
  result = ""
  for char in input_string:
    if char not in result:
      result += char
  return result

# Example usage
input_str = "mississippi"
output_str = remove_duplicates_loop(input_str)
print(f"Original string: {input_str}")
print(f"String with duplicates removed (using loop): {output_str}")