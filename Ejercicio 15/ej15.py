word = "invisible"
dictionary = {}

for i in word:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

print(dictionary)
print(max(dictionary, key = dictionary.get))