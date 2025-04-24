input_list=[5, 1, 4, 2, 8]
n = len(input_list)
new_list = list(input_list)

for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
print(new_list)