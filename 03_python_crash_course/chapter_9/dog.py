class Dog:
    ''' a simple dog'''

    def __init__(self, name, age):
        '''init name and age attributes'''
        self.name = name
        self.age = age

    def sit(self):
        '''dog sit command'''
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        '''dog roll over command'''
        print(f"{self.name} rolled over")

my_dog = Dog('Logan', 6)
print(f"My pup's name is {my_dog.name}, and he's {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()

