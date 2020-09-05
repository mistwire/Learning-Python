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

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"This animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
       # super changes context based upon what class is in () in the class definition
       # here super in the class Cat is referring to Animal
       super().__init__(name, species="Cat") # don't have to call self
       # Animal.__init__(self, name, species) # uncommon way of calling a parent class
       self.breed = breed
       self.toy = toy
    
    def play(self):
        print(f"{self.name} plays with {self.toy}")



soup = Cat("Soup", "mixed", "Fingers")

print(soup)
print(soup.species)
print(soup.breed)
print(soup.toy)
soup.play()
