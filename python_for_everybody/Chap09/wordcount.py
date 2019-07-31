counts = dict()
line = input("Enter a line of text: ")
words = line.split()

print('Words:', words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

''' use this text:
the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car
'''