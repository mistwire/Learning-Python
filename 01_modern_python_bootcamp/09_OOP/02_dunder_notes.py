# _name   <-- convention to let devs know that this is a private variable/property
# __name  <-- if you use 2 underscores, Python will behind the scenes change the name of the attribute (i.e. 'name mangling')
# __name__ <-- don't define methods with dunderscores until later (when we know what we are doing)


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

