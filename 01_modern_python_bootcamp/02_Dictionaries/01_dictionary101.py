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

