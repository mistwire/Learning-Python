# when you create a class, python looks for __init__ method, 
# which gets called every time you create an instance of the class (when you instantiate it)


class User:
    def __init__(self, first, last="default", age=46): # same rules apply as with defaul parameters
        # here is where you initialize the data that each new user has
        self.first = first # self refers to the current instance of the User class 
        self.last = last # assignments don't need to be named the same 
        self.age = age

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca")

print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)



