'''Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt '''


fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip()
    words = line.split()
    for word in words:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)

'''
fhand = open('mbox-short.txt')
for line3 in fhand:
    line3 = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line3.split()
    print(words[2])
'''