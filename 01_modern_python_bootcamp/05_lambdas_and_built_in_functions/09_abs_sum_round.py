# abs return the absolute value of a number.  Can be int or float
print(abs(5))
print(abs(-5))
print(abs(-5.345234))

# can use fabs (changes everything to float), but you need to import math 1st
print('\n')
# sum takes an iterable and an optional start
# returns the sum of start & the items of the iterable
# optional start defaults to 0

print(sum([12,23,54,23]))

print(sum([12,23,54,23], -1))

print(sum([12.23,23.12,54,23]))

print(sum([12.23,23.12,54,23], -112))


# round returns a rounded version, specify a number of digits for decimal, integer if none specified

print(round(3.51234))  #rounds to an integer

print(round(3.51234, 3)) # rounds to 3 decimal places

print(round(3.51234, None)) # rounds to an integer


# Write a function that accepts a single list full of numbers & returns the magnitude of the number with the largest magnitude:
# max_magnitude([300, 20, -900])  ->  returns 900
# max_magnitude([10,11,12])  -> returns 12
# max_magnitude([-5, -1, -89])  -> returns 89

def max_magnitude(l1):
    l2 = [abs(num) for num in l1]
    return max(l2)
    
def max_magnitude(l1):
    return max([abs(num) for num in l1])

def max_magnitude(l1):
    return max(abs(num) for num in l1)

# Write a function called sum_floats. 
# This function should accept a variable number of arguments. 
# The function should return the sum of all the parameters that are floats. 
# If there are no floats the function should return 0

def sum_floats(*args):
    total = 0
    for num in args:
        if isinstance(num, float):
            total += num
    return total

def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)