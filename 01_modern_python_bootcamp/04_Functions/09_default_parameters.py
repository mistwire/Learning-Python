

def exponent(num, power=2): #if no power is specified, power will default to 2
    return num ** power


print(exponent(2,3))
print(exponent(4,4))
print(exponent(7))


#pop method works like this, if you don't specify an index, it will default to the -1 index (last item), but you can override that and have it pop any indexed item:


countries = ['France', 'USA', 'Germany', 'Spain', 'Argentina']

print(countries.pop(0))
print(countries.pop())


# default parameters can be anything - lists, dicts, strings, booleans, even other functions:

def add(a,b):
    return a+b

def math(a,b, fn=add): # 3rd parameter is a function that defaults to the add function
    return fn(a,b)

def subtract(a,b):
    return a-b

print(math(2,2)) # gives you 4
print(math(4,2,subtract)) #gives you 2

# Write a function called speak that accepts a single parameter animal:
# Define speak below:
def speak(animal='dog'):
    if animal == 'pig':
        return 'oink'
    elif animal == 'duck':
        return 'quack'
    elif animal == 'cat':
        return 'meow'
    elif animal == 'dog':
        return 'woof'
    else:
        return '?'

#more compact version with a dictionary:
def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"


#even MORE compact version which passes in a default value to get() :
def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')