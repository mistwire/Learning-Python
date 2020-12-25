# more practice with dunder methods
# if you can modify existing ones with parent class attributes
# e.g. using the existing dict... but making it grumpy!

class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()
    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL IT'S AIN'T HERE!")
    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE IT AGAIN??")
        print("OK FINE.")
        super().__setitem__(key, value)
    



data = GrumpyDict({"first": "Tom", "animal": "Cat"})
print(data)
data['city'] = 'Tokyo'
print(data)


