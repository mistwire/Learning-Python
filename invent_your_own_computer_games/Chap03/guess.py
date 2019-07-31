#This is the guess the number game
import random

guessesTaken = 0

print('Hello!  What is your name?')
myName = input()

number = random.randint(1,20)
print("Well, " + myName + ", I'm thinking of a number between 1 and 20")

for guessesTaken in range(6):
    print('Take a guess')
    guess = int(input())

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break

if guess == number:
    print('Good job, ' + myName + '!  You guessed my number in ' + str(guessesTaken + 1) + ' guesses!')

if guess != number:
    print('Nope.  The number I was thinking of was ' +number+'.')
    
