# There is a lambda for each value in the iterable
# Returns filter object which can be converted into other iterables
# The object contains only the values that return True to the lambda

a_list = range(1,20)
evens = list(filter(lambda x: x%2 == 0, a_list))
print(evens)

# take a list of names and create a new list with only the names that start with 'a'
names = ["austin", "penny", "anthony", "angel", "chris", "billy", "steve"]
a_names = list(filter(lambda name: name[0] == 'a', names))
print(a_names)


# simple 'twitter' 
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))
print(inactive_users)

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]
print(inactive_users2)

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]
print(usernames2)

# combine filter and map given a list of names:
names = ['Lassie', 'Chris', 'Rusty', 'Colt']
# return a new list with the string 'Your instructor is ' + each value in array... but only if the val < 5 characters!

print(list(map(lambda name: f"Your instructor is {name}", 
	filter(lambda value: len(value) <= 5, names)))) #this is the collection that map is running on, a filter on names list


print(list(map(lambda user: user["username"].upper(),  #creates list of the username in uppercase
	filter(lambda u: not u['tweets'], users))))        # filters for users that have 0 tweets & passing into map


# OR just do a list comprehension

print([f"your instructor is {name}" for name in names if len(name) <= 5])

print([user['username'].upper() for user in users if not user["tweets"]])


