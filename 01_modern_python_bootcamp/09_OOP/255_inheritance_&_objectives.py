# Inheritance = the ability to define a class which inherits from another class (a 'base' or 'parent' class)
#  

class Animal:
    def make_sound(self, sound):
        print(f"this animal says {sound}")
    cool = True

class Cat(Animal): # Cat class inherits from the animal class
    pass # doesn't actually do anything itselff

a = Animal()
a.make_sound("chirp!")

soup = Cat()
soup.make_sound("meow")

print(soup.cool)
