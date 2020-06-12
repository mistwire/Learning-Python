#Sets are an unordered collection of data that does not have duplicate values
#Useful if you have data where you don't care about ordering, keys or values, & you don't want duplicates

#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()

s = set({1,2,3,4,5,5,5})
print(s) 
s = {1,2,'a', 'b', 23.33334}
print(s) 

for thing in s:
    print(thing)

# you are given a list & want to get unique values
numbers = [1,2,3,4,2,3,1,3,4,2,3,4,6,7,5,4,5,6,7,5,3,2,2]
print(set(numbers)) # gives you a set which returns unique data
print(list(set(numbers))) # turns set back into a list

print(len(set(numbers))) # gives number of unique datapoints

#Set Methods:
# Add - add data into a set
# if you try to add the same thing twice it won't do anything (duh)
s.add('add using add')
s.add(7)
print(s)

# Remove - removes a value from a set.
# KeyError if value isn't in set
s.remove(7)
print(s) 

# Discard - removes a value from a set
# Does not error if value isn't in set
s.discard(7)
s.discard('add using add')
print(s)

# copy - creates a copy of the set
another_s = s.copy()
print(another_s)

# clear - removes all the contents of the set
numbers_set = set(numbers)
print(numbers_set)
numbers_set.clear()
print(numbers_set)

# Set Math:
#"add" sets together without duplicates. '|' = set unions
math_students = {'Matthew', 'Helen', 'Prashant', 'Chris', 'James', 'Aparna'}
biology_students = {'Jane', 'Chris', 'Charlotte', 'James', 'Oliver', "Mesut", 'Matthew', 'Hunter'}
print(math_students | biology_students) # a set of all students without duplicates

print(math_students & biology_students) # a set of all students in both classes


friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

# intersection method gives you the values that are in 2 different sets:
print(friends_set.intersection(my_friends_set))

# difference method gives you the values that are not in both sets:
print(friends_set.difference(my_friends_set))

# union will add 2 sets togther:
print(friends_set.union(my_friends_set)) 

