#Create a function 'yell' which accepts a single string argument & returns an uppercased version of the string and an exclamation point at the end

#using string concatentation:
def yell(thing_to_shout):
    return thing_to_shout.upper() + '!'

print(yell("Who's a good boy?"))

#using an f-string:
def yell(word):
    return f'{word.upper()}!'

print(yell('get to the choppah'))