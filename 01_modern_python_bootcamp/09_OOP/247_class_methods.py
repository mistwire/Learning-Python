# Class methods are methods (with the @classmethod decorator) 
# that are not concerned with instances, but the class itself.
# Pretty rare in the wild & not commonly used... that being said here we go!

class User:

    active_users = 0 # Class attribute is defined outside of the class initializor or any methods

    @classmethod
    def display_active_users(cls): # cls is the standard, doesn't have to be cls
        print(cls)
        return f"There are currently {cls.active_users} active users"

    def __init__(self, first, last, age): # convention is __init__ goes @ the top of the class
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1 # this will increment active_users any time a User is initialized now.

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self): 
        return f"{self.first} {self.last}"

    def initials(self): 
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65 

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"


print(User.display_active_users())

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.display_active_users())
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.display_active_users())