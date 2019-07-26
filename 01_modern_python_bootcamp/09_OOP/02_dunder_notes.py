# _name   <-- convention to let devs know that this is a private variable/property
# __name 
# __name__


class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi!"
        self.__msg = "I like turtles!"

p = Person()
print(p.name)
print(p._secret) # this still works, it's just a convention. There is no private methods or attributes in Python
# print(p.__msg) # this won't work because of name mangling -> becomes '_Person__msg'

print(dir(p))

