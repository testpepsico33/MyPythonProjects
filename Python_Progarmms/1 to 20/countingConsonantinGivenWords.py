
vowels=['a','e','i','o','u']

word="Programming"

count=0

for character in word:
    if character not in vowels:
        count =count +1
print(count)
