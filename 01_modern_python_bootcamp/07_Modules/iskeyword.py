import keyword

def contains_keyword(*args):
    for arg in args:
        if keyword.iskeyword(arg):
            return True
    return False



print(contains_keyword("hello", "goodbye"))
print(contains_keyword("grizzly", "ignore", "return", "False"))
