# Custom For loop

def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("end of iterator")
            break

my_for("hello")
my_for([1,2,3,4,5])


def my_for2(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)

def square(x):
    print(x*x)

my_for2("Hello World!", print)
my_for2([1,2,3,4,5], square)