# max return the largest item in an iterable or the largest of 2 or more arguments 
# min return the smallest item in an iterable or the smallest of 2 or more arguments 

nums = [23, 46, 73, 345, 2, 43, 7, 86]
letters = ['a', 'b', 'c', 'd', 'e']
my_dict = {1:'a', 2:'b', 3:'c', 4:'d'}
my_tup = (1, 5, 92, 3)

print(max(3,67,99))  #99
print(max('c', 'd', 'a'))   #d
print(max(nums))   #345
print(max(letters))	#e 
print(max(my_dict)) #4
print(max(my_tup)) #92

print(min(nums)) #2
print(min(letters)) #a
print(min(my_dict)) #1
print(min(my_tup)) #1

names = ['Arya', 'Samson', 'Dora', "Tim", 'Ollivander', 'Chrisovalandis']

print(min(names)) #Arya (based on letter "size" not length)
print(max(names)) #Tim

# If you want to know the length:
print([len(name) for name in names]) #[4, 6, 4, 3, 10, 14]
print(min(len(name) for name in names)) #3

print(max(names, key=lambda name:len(name))) # max length for 'n'

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

print(min(songs, key=lambda song: song['playcount']))
print(min(songs, key=lambda song: song['playcount'])['title'])
print(max(songs, key=lambda song: song['playcount']))
print(max(songs, key=lambda song: song['playcount'])['title'])