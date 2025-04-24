# Define the filename and content to write
filename = "simple_output.txt"
content_to_write = "This is some simple text written to the file.\nAnother line of straightforward content."

# Open the file in write mode ('w')
file_write = open(filename, 'w')

# Write the content to the file
file_write.write(content_to_write)

# Close the file
file_write.close()

print(f"Successfully wrote content to '{filename}'.")

# Open the same file in read mode ('r')
file_read = open(filename, 'r')

# Read the entire content of the file
file_content = file_read.read()

# Close the file
file_read.close()

print(f"\nContent read from '{filename}':")
print(file_content)