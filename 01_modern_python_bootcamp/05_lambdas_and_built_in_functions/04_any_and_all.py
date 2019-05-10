# all takes an iterable and returns True if all elements are truthy
# if the iterable is empty, return True
print(all([char for char in 'eio' if char in 'aeiou']))
# returns True because eio are all in aeiou
print([num for num in [4,2,6,8,6,10] if num % 2 == 0])
# no falsey values
print(all([num for num in [4,2,6,8,6,10] if num % 2 == 0]))
# returns True
print(all([num for num in [4,0,2,6,8,6,10] if num % 2 == 0]))
# returns False
print(all([])) #returns True

# any takes an iterable and returns True if any elements are truthy
# if the iterable is empty, return False

print(any([0, 1, 2, 3])) # True
print(any(val for val in [1,2,3] if val > 2)) # True
print(any(val for val in [1,2,3] if val > 5)) # False
