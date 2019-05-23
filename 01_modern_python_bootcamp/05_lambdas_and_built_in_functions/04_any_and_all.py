# all takes an iterable and returns True if all elements are truthy
# if the iterable is empty, return True

print(all([char for char in 'eio' if char in 'aeiou'])) # returns True because eio are all in aeiou

print([num for num in [4,2,6,8,6,10] if num % 2 == 0])  # no falsey values

print(all([num for num in [4,2,6,8,6,10] if num % 2 == 0]))   # returns True

print(all([num for num in [4,0,2,6,8,6,10] if num % 2 == 0]))  # returns False

print(all([])) #returns True



people = ["Charlie", "Casey", "Cody", "Carly", "Chris"]
print(people)
print(all(name[0]=='C' for name in people)) # returns True, all names start with 'C'
people.append("Mike")
print(people)

print(all(name[0]=='C' for name in people)) # returns False now becuase fuck Mike


# any takes an iterable and returns True if any elements are truthy
# if the iterable is empty, return False

print(any([0, 1, 2, 3])) # True
print(any(val for val in [1,2,3] if val > 2)) # True
print(any(val for val in [1,2,3] if val > 5)) # False

any(val for val in [1,2,3] if val > 5)
print(val for val in [1,2,3] if val > 5) # without 'any' this is actually a generator expression

# Implement a function 'is_all_strings' that accepts a single iterable and returns True if it contains ONLY strings
# otherwise return False
def is_all_strings(a_list):
    return all([type(i) is str for i in a_list])  # list comprehension

def is_all_strings(a_list):
    return all(type(i) is str for i in a_list) # generator expression 