#opening a file done with the open() function
#handle = open(filename, mode)
fhand = open('mbox.txt','r')
print(fhand)
#fhand = open('stuff.txt')

#the newline Character
stuff = 'Hello\nWorld!'
print(stuff)
stuff = 'X\nY'
print(stuff)
print(len(stuff))
# \n counts as 1 character

#Reading files in Python
#File handle as a squence
xfile = open('short.txt')
for cheese in xfile:
    print(cheese)

#counting the lines in a file
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count+1
print("Line Count:", count)

#Reading the whole file
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

#Searching through a file (fixed to clean out newline)
fhand = open("mbox-short.txt")
for line in fhand:
    #rstrip takes out the newline @ the end of a line
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)


#Skipping with continue:
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    print(line)

#Using in to select lines:
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

#To prompt for a filename:
fname = input("Enter the file name:  ")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject lines in", fname)

#What if the user puts in a bad filename?
fname = input("Enter the file name:  ")
#thrown in a try/except block!
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject lines in", fname)