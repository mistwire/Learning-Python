#Coin Toss Function
from random import random

def flip_coin():
    # generate a random number 0-1
    if random() > 0.5:
        return 'Heads'
    else:
        return 'Tails'

print(flip_coin())