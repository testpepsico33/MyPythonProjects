array = [1, 3, 55, 2, 7, 1, 9, 4, 2, 4, 9, 3, 1, 2, 6]
duplicates = set()
seen = set()
for item in array:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)
print(f"The duplicate values in the array are: {duplicates}")