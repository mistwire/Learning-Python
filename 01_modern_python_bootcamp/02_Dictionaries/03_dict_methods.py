instructor = {'name': "Chris",
              'owns_cat': True,
              'num_courses': 4,
              'favorite_language': 'Python',
              'is_short': False,
              69: 'hehehehehe'
              }

# clear - empties out the dictionary
d = dict(a=1, b=2, c=3)
d.clear()
print(d)

# copy - makes a copy of a dictionary
d = instructor.copy()
print(d)
print(d is instructor) #copies are in unique memory space therefor is resolves to False

# fromkeys - creates key-value pairs from comma separated values, any iterable collection in 1st space will work (string, list, range, etc...)

print({}.fromkeys('a', 'v'))
print({}.fromkeys('hello', '1'))
print({}.fromkeys('a', [1,2,3,4,5]))
print({}.fromkeys(['name : ', 'age : ', 'location : ' ], 'unknown'))
print({}.fromkeys(range(0,10), 'unknown'))

# get - retrieves value from key in a object, returns None if key doesn't exist

print(instructor.get('name'))
print(instructor.get('eggplant'))

# pop - have to provide key, returns value.  KeyError if you try to pop something that doesn't exist
print(instructor.pop('favorite_language'))

# popitem - removes a random k,v pair from a dictionary

print(instructor.popitem())

# update - update keys & values in a dictionary with another set of k/v pairs, will also overwrite existing if you use the same key.  Does not remove
print(instructor)
person = {'system' : 'laptop', 'favorite_color' : 'magenta'}
person.update(instructor)
print(person)

