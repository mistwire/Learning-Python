# Think of it as a function that has no name

# This is review:
def square(num):
    return num * num

print(square(9))


# This is a little shorter but does the same thing:
def square(num): return num * num


''' The syntax is 
lambda (parameter): (single expression)

'''


# This also does the same thing:
square2 = lambda num: num * num
# Typically you don't store the result in a variable, this is for demo purposes
print(square2(7))

add = lambda a,b: a + b

print(add(3,10))

# To prove that lambdas have no name: 
print(square.__name__)
print(square2.__name__)
print(add.__name__)

# Use case when you need to pass a function into another function as a parameter and that function will never be used again

import tkinter as tk
# Don't worry about any of this code
root = tk.Tk()#=====================
frame = tk.Frame(root)#=============
frame.pack()#=======================
# Don't worry about any of this code

'''
def say_hi(): #this function is only used once here, so let's make it a lambda!
    print("HELLO!")
'''
button = tk.Button(frame, 
                    text="CLICK ME", 
                    fg="red", 
                    command=lambda: print("Hello!")) # Now it's a lambda!

# Don't worry about any of this code
button.pack(side=tk.LEFT)#==========
root.mainloop()#====================
# Don't worry about any of this code
