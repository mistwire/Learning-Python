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
d = dict()
d['csev'] = 2
d['cwilly'] = 4
for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)

#Tuples are Comparable: goes from left to right in the comparision, if it finds one that is true, then it stops looking
print((0,1,2) < (5,1,2)) #comes back true because of [0]
print((0,1,20000) <(0,3,4)) #comes back true because of [1]
print(('Jones', 'Sally') < ('Jones', 'Sam')) #comes back true because of 1st 'l' in Sally is less than m in Sam

#Sorting lists of Tuples:
d = {'a':10, 'c': 22, 'b':1}
print(d.items())
print(sorted(d.items()))

t = sorted(d.items())
t
for (k,v) in sorted(d.items()):
    print(k,v)

#Sort by value instead of key:
c={'a':10, 'b':1, 'c':22}
tmp = list()
for (k,v) in c.items():
    tmp.append((v,k))
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)





