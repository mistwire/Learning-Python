'''
Multiple inheritance is not often used. Complexity scales up *quickly* when inheriting from multiple classes.

'''

class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"


class Ambulatory:
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"

class Penguin(Ambulatory, Aquatic): # Order matters here! only the __init__ for the 1st super class is called 
    def __init__(self, name):
        super().__init__(name=name)

jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captian Cook")

print(captain_cook.swim()) # gets method from Aquatic class
print(captain_cook.walk()) # gets method from Ambulatory class

# what happens when you call the greet method?
print(captain_cook.greet()) # gets from the Ambulatory method? Why?

print(f"capatin_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(f"capatin_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
print(f"capatin_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")