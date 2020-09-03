# class Human:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age


# jane = Human("Jane", "Goodall", 50)
# print(jane.age)

# #right now, anyone can manipulate age to be whatever they want:
# jane.age = -100
# print(jane.age)

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age #this implies "private"
        else:
            self._age = 0
    
    # def get_age(self):
    #     return self._age

    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    @property # this is a decorator - alters how this function works
    def age(self): # the name of this method is what you would now call to "get age"
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be negative!")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter # this isn't a great example, but shows the setter attribute for the property full_name 
    def full_name(self, name):
        self.first, self.last = name.split(" ")

jane = Human("Jane", "Goodall", -50)
# print(jane.get_age())
# jane.set_age(45)
# print(jane.get_age())

print(jane.age)
jane.age = 20
print(jane.age)
# jane.age = -1 # now this raises an error from the @age.setter decorator
print(jane.full_name)

jane.full_name = "Tim Minchin" # this uses the @full_name.setter property to set the name to Tim Minchin now

print(jane.__dict__)
print(jane.full_name)


