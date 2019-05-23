# a built-in function that will return a new sorted list from the items in an iterable:

more_numbers = [6,1,8,2]
print(more_numbers)
print(sorted(more_numbers))
print(more_numbers)

nums = [4, 3, 124, 2, 84, 23, 55, 29]
print(nums)
nums.sort() # sorts the original list
print(nums)

nums = [4, 3, 124, 2, 84, 23, 55, 29]
print(sorted(nums)) # prints a copy of the list, but original nums stays unsorted
print(nums)


my_tuple = (200,31,5,62,9,12)
print(my_tuple)
print(sorted(my_tuple)) # returns a sorted list 

# what if you want to sort something more complex by username?
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple", "num": 10},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

print(sorted(users, key=len)) # runs len on every dict in the list - sorts by # of keys

print(sorted(users, key=lambda user: user['username'])) # Sort by username

print(sorted(users, key=lambda user: len(user['tweets']))) # sort by number of tweets

print(sorted(users, key=lambda user: len(user['tweets']), reverse=True)) # most active to least active tweeter :-) 




