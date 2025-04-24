
input_list = [1, 2, 2, 3, 4, 4, 5, 1]
seen = set()
unique_list = []
for item in input_list:
    if item not in unique_list:
        seen.add(item)
        unique_list.append(item)
print(unique_list)
print(seen)