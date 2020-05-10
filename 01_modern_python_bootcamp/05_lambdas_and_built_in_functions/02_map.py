# map
# a standard function that accepts at least 2 arguments: 
# 1. a function (usually a lambda)
# 2. an 'iterable' (list, string, dict, set, tuple)
# runs the function/lambda for each value in the iterable and returns a map object which can be converted into another data structure
nums = [2, 4, 6, 8, 10]
print(nums) #prints the map object, not the manipluated values

doubles = map(lambda x: x*2, nums)
'''Syntax:
map(lambda parameter:expression, iterable)
'''

print(doubles) # get back a map object that you can iterate over
for num in doubles:
    print(num)

# only works once, if you try to call it again it comes back as an empty list:
print(list(doubles)) # empty list now

# usually what you will do is cast it as a list immediately:
triples = list(map(lambda x: x*3, nums))

print(triples)


people = ["Darcy", "Christina", "Dana", "Annabel"]

peeps = map(lambda name: name.upper(), people)
print(list(peeps))

names = [
    {'first':'Rusty', 'last':'Steele'}, 
    {'first':'Chris', 'last':'Williams'}, 
    {'first':'Blue', 'last':'Steele'}
]
first_names = list(map(lambda x: x['first'] + ' ' + x['last'], names))
print(first_names)

# decrement list - define a function that takes a list of numbers and decrements each value by 1
def decrement_list(a_list):
    return list(map(lambda num: num-1, a_list))

print(decrement_list([4,2,86,43,90]))