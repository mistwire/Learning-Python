# immutable, ordered collection or grouping of items

my_1st_tuple = (1, 'a', 3,['b', 'c', 'd'],3,3, 4) 
print(my_1st_tuple[1])
print(my_1st_tuple[3])


x = (1, 2, 3)
print(3 in x)  # True


# tuples are faster than lists because they don't change
#.items() on a dictionary returns a tuple
cat = {'name' : 'Stinky Bean', 'age' : 13, 'Is Scared?' : True}

print(cat)
print(cat.items())


months = ('January', 'February', 'March', 'April')


#can use a tuple as the key in a dictionary:
location = {
    (35.68, 39.69) : "Tokyo Office",
    (40.71, 74.00) : 'New York Office',
    (37.77, 122.41) : "San Francisco Office"
}
print(location)


#Iterating over a tuple (just like a list):
for month in months:
    print(month)


#Tuples 2 built in methods:
#count returns the number of times a value appears in a tuple:
x = (1,1,2,3,3,3,4,5,5,5)
print(x.count(1)) #returns 2
print(x.count(3)) #returns 3
print(x.count(5)) #returns 3

#index returns the index at which a value is found in a tuple
#errors out if not in the tuple
#only returns the index of the 1st value if multiple
print(x.index(5)) #returns 7

# You can also slice tuples

