# take each list element and square it
numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
  squares.append(n**2)

print(squares)

# list comprehension version:
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers] 

print(squares)  # Output: [1, 4, 9, 16]


# Write a function that accepts a list of values and returns a list of only the truthy values:
#  i.e.  pass in compact([0, 1, 2, "",[], False, {}, None, "All done"]) and get back [1, 2, "All done"]
# for loop version:

def compact(a_list):
    truthy_list = []
    for val in a_list:
        if val:
            truthy_list.append(val)
    return truthy_list
    pass

# list comprehension version:

def compact(a_list):
    return [val for val in a_list if val]


# create a function that takes in a list and a callback function.  The callback returns True or False.  
# The function should iterate over the list and invoke the callback function at each iteration.
# if the callback returns True, the element should go into a 'truthy' list
# if the callback returns False, the element should go into a 'falsey' list
# when it's finished, the function returns both lists in one larger list

def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]

# list comprehension version:

def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


