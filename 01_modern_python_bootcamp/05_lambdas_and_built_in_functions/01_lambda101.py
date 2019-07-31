# Think of it as a function that has no name

# This is review:
def square(num):
    return num * num

print(square(9))


# This is a little shorter but does the same thing:
def square(num): return num * num


# This also does the same thing:
square2 = lambda num: num * num
# Typically you don't store the result in a variable, this is for demo purposes
print(square2(7))

add = lambda a,b: a + b

print(add(3,10))

print(square.__name__)
print(square2.__name__)
print(add.__name__)

# Use case when you need to pass a function into another function as a parameter and that function will never be used again


