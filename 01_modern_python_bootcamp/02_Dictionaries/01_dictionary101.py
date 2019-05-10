instructor = {'name': "Chris",
              'owns_cat': True,
              'num_courses': 4,
              'favorite_language': 'Python',
              'is_short': False,
              69: 'hehehehehe'
              }

print(instructor)


# add item to dictionary
cat = dict(name="Soup", age = 9)
print(cat)
cat['is_cute'] = True
print(cat)

print(instructor['name'])


# get from dict


# print(instructor['thing'])  #this will create a KeyError

artist = {
    "first": "Neil",
    "last": "Young",
}
full_name = artist['first'] + ' ' + artist['last']

#Using a for loop to iterate over a dictionary:
#Get all values:
print(instructor.values())
for value in instructor.values():
    print(value)

#Get all keys
print(instructor.keys())
for keys in instructor.keys():
    print(keys)

#Get both
print(instructor.items())
for k,v in instructor.items():
    print(f'{k} is the key and {v} is the value')

 
#test for the existence of a key in a dictionary without getting a KeyError
print('name' in instructor)
print('cat' in instructor)

# Calculate Walkthrough 
# This solution uses dict.get() a lot. dict.get('first')  will return the value of 'first' if it exists, otherwise it returns None.  However, you can specify a second argument which will replace None as the default value. I use that in this solution a bunch of times.
# I defined a dictionary called operation_lookup  that maps a string like "add" to an actual mathematical operation involving the values of 'first' and 'second'
# I create a boolean variable called is_float, which is True if kwargs contains 'make_float', otherwise it's false
# Then I lookup the correct value from the operation_lookup dict using the operation that was specified in kwargs
# Basically, turning something like "subtract" into:kwargs.get('first', 0) - kwargs.get('second', 0) 
# Which in turns simplifies to a number
# I store the result in a variable called operation_value 
# I return a string containing either the specified message or the default 'The result is' string.  
# Whether operation_value  is interpolated as a float or int is determined by the is_float  variable.
# Note: this solution will divide by zero if a 2nd argument isn't provided for divide.  You may want to change the default value to 1.  We learn how to handle ZeroDivisionErrors later on in the course.  Thanks, Scott for pointing out the issue!
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final

print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"