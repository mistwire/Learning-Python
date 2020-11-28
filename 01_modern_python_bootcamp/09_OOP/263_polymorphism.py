# poly = many
# morph = shapes or forms

# 2 Practical applications:
# 1. the same class method works in similar way for diff classes
# have a method in the base (or parent) class that is overridden by a subclass. 
# this is called method overriding
# Example
# Cat.speak() # meow
# Dog.speak() # woof
# Human.speak() # yo

class Animal():
    def speak(self):
        # common pattern to force subclasses to define method there
        raise NotImplementedError("Subclass needs to implement this method") 

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

class Fish(Animal):
    pass

d = Dog()
print(d.speak())

f = Fish()
print(f.speak()) #this will throw an error because there is no speak method in the Fish subclass



# 2. the same operation works for diff kinds of objects
# Example 
# len() can work on lists, strings, tuples, etc...

