def first_non_duplicate(text):
    counts = {} #An empty dictionary is created to store character counts.
    for char in text:
        if char in counts:#If "yes," increment the existing count.If "no," add the character to the tally sheet with a count of 1.
            print(char)
            print(counts)
            counts[char] += 1
            print(counts)
        else:
            counts[char] = 1
    for char in text:
        if counts[char] == 1:
            return char
    return None

string = "NirmalKumar"
print(first_non_duplicate(string))

