#Lists

print ([1,24,76])
print ([1,[5,6],7])
print(['red', 'yellow', 3])

for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')

friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])

#Lists are mutable, strings are not:
lotto = [2,14,26,41,63]
print(lotto)
lotto[2] = 28
print(lotto)

#How long is a list?
greet = 'Hello Bob'
print(len(greet))
x = [1,2,'joe',99]
print(len(x))  #len gives you the number of things in the list

#using the range function -> returns a list of numbers that range from 0 to one less than the parameter:
print(range(4))
print(len(friends))
print(range(len(friends)))

#A tale of 2 loops:
for friend in friends:
    print('Happy New Year: ', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year: ', friend)

#Concatenating lists using + 
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

#Lists can be sliced using:
t = [9,41,12,3,74,15]
print(t[1:3]) #up to but not including :-) 
print(t[:4])
print(t[3:])
print(t[:])

#List Methods
x=list()
print(type(x))
print(dir(x)) 

#Building a list from scratch
stuff = list() #constructor form
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

#is something in a list?
some = [1,9,21,10,16]
print(9 in some)
print(15 in some)
print (20 not in some)

#lists are in order and are sortable:
friends.sort()  # call the sort method
print(friends)
print(friends[1])

#Built in functions and lists:
nums = [3,41,12,9,74,15]
print(len(nums))
print(max(nums)) # find largest
print(min(nums)) #find the smallest
print(sum(nums)) #add em all together
print(sum(nums)/len(nums)) #get the average of all the numbers

#How are strings and lists related?
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[1])
for w in stuff:
    print(w)

line = "A lot                   of     spaces" #multiple spaces are treated like 1 delimiter
etc = line.split()
print(etc)

line2 = 'first;second;third'
thing = line2.split() 
print(thing)
thing = line2.split(';') #you can specify your delimiter
print (thing)
print(len(thing))

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words)

'''
fhand = open('mbox-short.txt')
for line3 in fhand:
    line3 = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line3.split()
    print(words[2])
'''

#the double split pattern
line4 = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line4.split()
email = words[1]
print(email)
pieces = email.split('@')
print(pieces[1])

