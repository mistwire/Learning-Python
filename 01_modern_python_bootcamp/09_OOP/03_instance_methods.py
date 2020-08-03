# now we're going to talk about instance methods
# this is where OOP becomes a lot more useful than just organizing data
# instance methods are different from class methods (more on those later)


class User:
    def __init__(self, first, last, age): # convention is __init__ goes @ the top of the class
        self.first = first
        self.last = last
        self.age = age

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

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(user2.full_name())
print(user1.initials())
print(user2.initials())
print(user1.likes("Ice Cream"))
print(user2.likes("Chips"))

print(user2.is_senior())
print(user1.age)
print(user1.birthday())
print(user1.age)
