# going to create a class attribute that allows us to store a list of the permitted species
class Pet:
    allowed = [ 'cat', 'dog', 'fish', 'rat'] # class attribute that only allows these types of pets
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!") 
        self.name = name
        self.species = species




cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")

