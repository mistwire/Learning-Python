# behind the scenes dunder methods
# the plus sign '+' -> 8+2=10   but   "8" + "2" = 82
print(8 + 2)
print("8" + "2")
# the + operator is shorthand for a special method called __add__() that gets called on the 1st operand
# if the first (left) operand is an int, __add__() does math
# if the first (left) operand is a string, __add__() does concatenation
# You can declare special methods on your own classes to mimic the behavior
# of builtin objects, like so using __len__:
class Human():
    def __init__(self, height, name="somebody"):
        self.height = height
        self.name = name
    def __len__(self):
        return self.height

# String Representation Example:
# The __repr__ method is one of several ways to provide a nicer string representation:
    def __repr__(self):
        return self.name




Chris = Human(78)
print(Chris)
print(f"Chris is {len(Chris)} inches tall!")

Kim = Human(67, "Kim")
print(Kim)
print(f"Kim is {len(Kim)} inches tall!")


