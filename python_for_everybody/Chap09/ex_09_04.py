'''
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
names = list()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    author = line.split()
    names.append(author[1])
#print(names)
for name in names:
    counts[name] = counts.get(name, 0) + 1
#print(counts)

largest = -1
theword = None
for k,v in counts.items():
    # print(k,v)
    if v > largest:
        largest = v
        theword = k #capture, remember the key that was largest

print(theword, largest)