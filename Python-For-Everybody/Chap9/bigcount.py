name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
filename = open(name)

counts = dict()
for line in filename:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
