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
# https://docs.python.org/3/reference/datamodel.html#object.__repr__ 
    def __repr__(self):
        return self.name

Chris = Human(78)
print(Chris)
print(f"Chris is {len(Chris)} inches tall!")

Kim = Human(67, "Kim")
print(Kim)
print(f"Kim is {len(Kim)} inches tall!")


from copy import copy 
class Human2:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age # here we're calling len the age of a human so it will return 47

    def __add__(self, other):
        # when you add 2 humans, it creates a new 0 len human with last name of 1st human & no 1st name :-) 
        if isinstance(other, Human2): 
            return Human2(first='Newborn', last = self.last, age = 0)
        return "You can't add that!"

    # ok now lets CLONE humans! :-) 
    def __mul__(self, other):
        # return "You are cloning humans!"
        if isinstance(other, int):
            return [copy(self) for i in range(other)] # use copy otherwise you get X number of pointers to the same object
        return "Can't clone" # for anything other than int

j = Human2("Jenny", "Larson", 47)
k = Human2("Kevin", "Jones", 49)
print(j) 
print(len(j)) 
print(j + k)
print(j * 2)

# K and J having triplets :-) 
triplets = (k + j) * 3
print(triplets)
