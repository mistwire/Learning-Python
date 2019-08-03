# Define attribute directly on a class that are shared by all instances of a class and the class itself.
# Class attributes and methods are used far less often than instance attributes & methods.

class User:

    active_users = 0 # Class attribute is defined outside of the class initializor or any methods

    def __init__(self, first, last, age): # convention is __init__ goes @ the top of the class
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1 # this will increment active_users any time a User is initialized now.

# methods are written just like regular functions... but they become methods when written inside of a class
    def full_name(self): # difference - still need to provide self
        return f"{self.first} {self.last}"

    def initials(self): # self will *always* be the 1st parameter in any instance method
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65 # this is a boolean expression that will return True or False

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"


print(User.active_users)

