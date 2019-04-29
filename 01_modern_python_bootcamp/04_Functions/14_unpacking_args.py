# using * as an Argument:
# Argument Unpacking
# We can use * as an argument to a function to 'unpack' values

def sum_all_values(*args):
    total = 0
    for num in args:
        total += num # can't add an int and a ['list'] or (tuple,)
    print(total)

nums = [1, 2, 3, 4, 5, 6, 7]
sum_all_values(*nums) # if you have a list of things that you want to unpack & send to a function NOT expecting a list

# works with tuples too
nums = (4,7,89,3,6,45,24)
sum_all_values(*nums)

# Using ** as an argument
# Dictionary Unpacking 
