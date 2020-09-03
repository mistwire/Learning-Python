# Animal
#     species
#     name 

# Cat 
#     species
#     name 
#     breed 
#     favorite toy



class Animal:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Animal):
    pass

soup = Cat()


