
number_list = [3, 7, 1, 9, 4, 1, 6]
min_val = number_list[0]
max_val = number_list[0]
for num in number_list:
    if num < min_val:
      min_val = num
    if num < max_val:
      max_val = num
print(min_val, max_val)