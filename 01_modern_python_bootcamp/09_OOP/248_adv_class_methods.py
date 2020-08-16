# A more common (but advanced) example of class methods


class User:

    active_users = 0 # Class attribute is defined outside of the class initializor or any methods

    @classmethod
    def display_active_users(cls): # cls is the standard, doesn't have to be cls
        print(cls)
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",") #splits the string on , and feeds the 3 variables
        return cls(first, last, int(age))
    
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

# Say we have data that is arriving in a not formatted (but common) format like "Tom, Jones, 89"

user1 = User.from_string("Tom, Jones, 89")
print(user1.first)
print(user1.full_name())
print(user1.birthday())







# Another example is dict.fromkeys().  
# (dict is a class even though it's not capitalized)

user = dict.fromkeys(['name', 'age', 'city'], 'unknown')
print(user)