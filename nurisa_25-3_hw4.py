data_tuple = ('h', 6.13, 'C', 'e', 'T',True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
    if type (i) == str:
        letters.append(i)
    else:
        numbers.append(i)

numbers.remove(6.13)
letters.append(numbers.pop(0))
numbers.insert(1,2)
numbers.sort()
letters.reverse()
letters[1] = "G"
letters[7] = "c"

for i in range(len(numbers)):
    numbers[i] *= numbers[i]
word = tuple(letters)
word1 = tuple(numbers)

print(word1)
print(word)
