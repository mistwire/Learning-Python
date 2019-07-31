from random import random

def flip_coin():
    # generate a random number 0-1
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"

print(flip_coin())

# refactor:
def flip_coin(): # if you re-def a function, the original is ignored
    # generate a random number 0-1
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"

print(flip_coin())

