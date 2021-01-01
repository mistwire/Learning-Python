# generators are iterators
# not all iterators are generators
# regular functions use return keyword
# generator functions use the yield keyword
# can be created with generator expressions

# our 1st generator

def count_up_to(max):
    count = 1
    while count <= max:
        yield count # this is the only new part of this function
        count +=1 
# returns the value of count one at a time

print(count_up_to(5)) # shows a generator object 

counter = count_up_to(5) 

help(counter)

print(next(counter)) # gives ONE item then stops
print(next(counter)) # gives ONE item then stops
print(next(counter)) # doesn't keep all of the numbers in memory
print(next(counter)) # just the next one in the generator to yield 
print(next(counter))
# print(next(counter)) # until we get to a StopIteration error
print("\n")

counter = count_up_to(10)
print(next(counter))
print("now we start a loop, but it starts @ 2 because of line 30")
for num in counter:
    print(num)

print("A for loop catches the StopIteration & breaks, manually doing next() will not")

counter = count_up_to(15)
print(list(counter)) # if we want all the values in a generator all at the same time, we can convert to list
