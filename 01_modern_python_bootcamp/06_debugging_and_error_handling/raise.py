def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta') # tuple of valid colors
    if type(color) is not str:
        raise TypeError("color must be a string")
    if type(text) is not str:
        raise TypeError("text must be a string")
    if color not in colors:
        raise ValueError('color is invalid color')

    print(f"Printed {text} in {color}")

colorize("hello", "red")


