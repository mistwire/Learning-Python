def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Don't divide by zero please")
    except TypeError as err: #saves the TypeError as a variable err
        print("a and b must be ints or floats")
        print(err) # prints out the TypeError
    else:
        print(f"{a} divided by {b} is {result}")


print(divide(1,2))
print(divide(1,0))
print(divide(1,'a'))

