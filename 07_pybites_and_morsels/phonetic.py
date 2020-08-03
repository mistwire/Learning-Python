
import sys

phonetics = {
    'a': "Alfa",
    'b': "Bravo",
    'c': "Charlie",
    'd': "Delta",
    'e': "Echo",
    'f': "Foxtrot",
    'g': "Golf",
    'h': "Hotel",
    'i': "India",
    'j': "Juliett",
    'k': "Kilo",
    'l': "Lima",
    'm': "Mike",
    'n': "November",
    'o': "Oscar",
    'p': "Papa",
    'q': "Quebec",
    'r': "Romeo",
    's': "Sierra",
    't': "Tango",
    'u': "Uniform",
    'v': "Victor",
    'w': "Whiskey",
    'x': "X-ray",
    'y': "Yankee",
    'z': "Zulu",
}

words = " ".join(sys.argv[1:])
if not words:
    words = input("Text to spell out: ")
for char in words.lower():
    if char in phonetics:
        print(phonetics[char])