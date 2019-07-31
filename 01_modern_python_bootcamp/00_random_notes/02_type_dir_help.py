# Using type(), dir(), and help()
# We can use three very useful methods in the REPL to help us understand our Python programs.
# Pass in an object into the type() Use type to find the type of an object in Python.

name = "Chris"
print(type(name))

# We’ll see that the type is str, Python’s version of a string. 
# Now that we know this object’s type, we can pass the type into other methods.
# The first one is dir() which stands for directory. 
# If we check the type of str (notice, no quotes here)) in the REPL, we’ll see all the methods available on strings in Python. 

print(f"\n{dir(str)}")
print(f"\n{dir(list)}")

# The next useful method is help(). 
# You can a type, method, or other object to help to instantly see available documentation about the method, the parameters it expects, and what it returns.
# Let’s try this in the REPL, and look up the documentation for the isupper method in String. 
# We access it with the period symbol (.). This is called dot-notation.

print(f"\n{help(str.isupper)}")
