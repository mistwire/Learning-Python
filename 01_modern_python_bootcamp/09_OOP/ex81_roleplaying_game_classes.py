class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

 
class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return f"{self.name} says: 'Here is your quest!'" 



u1 = Character("Chris", 100, 2)
print(u1.name)
print(u1.level)
print(u1.hp)

npc1 = NPC("Steve", 10000, 40)
print(npc1.name)
print(npc1.level)
print(npc1.hp)
print(npc1.speak())
