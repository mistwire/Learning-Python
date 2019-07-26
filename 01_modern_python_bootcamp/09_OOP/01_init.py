class User:
    def __init__(self, first, last="default", age=46):
        self.first = first
        self.last = last
        self.age = age

user1 = User("Joe")
user2 = User("Blanca")

print(user1.first, user1.last)
print(user2.age)



