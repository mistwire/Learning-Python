# Iterator - an object that can ben iterated upon. An object that returns data, one element at a time, when next() is called on it
# Iterable - an object which will return an Iterator when iter() is called on it

# "HELLO" is an interable, but it is NOT an iterator
# iter("HELLO") returns an iterator 

name = "Oprah"
it = iter(name)
print(next(it))

# when next() is called on an iterator, the iterator returns the next item over and over until it raises a StopIteration error

for char in it: # notice this starts at "p" because the first letter was next()'ed on line 9
    print(char)

nums = [1,2,3,4,5]
nums_iter = iter(nums)
print(type(nums_iter))

