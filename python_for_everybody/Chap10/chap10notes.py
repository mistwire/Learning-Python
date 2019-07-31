#Tuples - function like lists except that they can't be changed
x = ('Glenn', 'Sally', 'Joe')
print(x[2])

y = (1,9,2,4,6,8,3,55)
print(max(y))
for i in y:
    print(i)

# HOWEVER - you can't change a tuple, uncomment the following lines to crash this script:
'''
y = ("a", "b", "c")
y[2] = ('d')
print(y)
'''
# you cannot sort, append or reverse a tuple - anything having to do with changing the tuple

l = list()
print(dir(l))
print()
t = tuple()
print(dir(t))

#Tuples and Assignment - can put a tuple on the left hand side of an assignment statement
(x,y) = (4,'fred')

print(y)
print(x,y)

#Tuples and Dictionaries:
d = dict() #create an empty dictionary
d['csev'] = 2 #add a key value pair 
d['cwilly'] = 4  #add another key value pair 
for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)

#Tuples are Comparable: goes from left to right in the comparision, if it finds one that is true, then it stops looking
print((0,1,2) < (5,1,2)) #comes back true because of [0]
print((0,1,20000) <(0,3,4)) #comes back true because of [1]
print(('Jones', 'Sally') < ('Jones', 'Sam')) #comes back true because of 1st 'l' in Sally is less than m in Sam

#Sorting lists of Tuples:
d = {'a':10, 'c': 22, 'b':1} # create your dictionary
print(d.items()) # sorting will come out as whatever because it's a dictionary
print(sorted(d.items())) # sorted will sort by keys (if all keys are the same it'll sort by values)

#Using sorted()
t = sorted(d.items())
t
for (k,v) in sorted(d.items()):
    print(k,v) #print key then value
    print(v,k) #print value then key

#Sort by value instead of key:
c={'a':10, 'b':1, 'c':22}
tmp = list()
for (k,v) in c.items():
    tmp.append((v,k))
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

#Print top 10 most common words in a file
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1 #know this idiom!

lst = list()
for key,val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val,key in lst[:10]:
    print(key,val)


#Even shorter version:
print(sorted ( [(v,k) for k,v in c.items()]))

# http://wiki.python.org/moin/HowTo/Sorting
