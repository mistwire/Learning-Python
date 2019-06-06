# how to handle an error
# right now our code kicks out an error & breaks the program

try:
    foobar
except:
    print("PROBLEM!")

try:
    foobar
except NameError as err:
    print(err)
print("after the try")

try:
    colt
except: # never do this because it will catch ALL errors and print the following, even if it's a diff type of error
    print("You tried to use a variable that was never declared")


d = {"name": "Chris"}

def my_get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

print(my_get(d, "name"))
print(my_get(d, "city"))
