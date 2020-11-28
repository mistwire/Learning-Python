# Method Resultion Order (MRO)
# Whenever you create a class, Python sets a MRO for that class, which is the order in which Python will look for methods on instances of that class.
# you can programmatically reference MRO in 3 ways:
# __mro__ attribute on the class
# use the mro() method on the class
# use the builtin help(cls) method  <-- most human readable way 

class A:
    def do_something(self):
        print("Method Defined In: A")

class B(A):
    def do_something(self):
        print("Method Defined In: B")

class C(A):
    def do_something(self):
        print("Method Defined In: C")   

class D(B,C):
    def do_something(self):
        print("Method Defined In: D")

thing = D() 
thing.do_something() # will pring method defined in D

print(D.__mro__) # shows order but is kinda ugly

print(D.mro()) # same format as __mro__

help(D) # best for human readable


