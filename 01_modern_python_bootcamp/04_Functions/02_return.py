def print_square_of_7():
    print(7**2)
print_square_of_7()

def square_of_7():
    7**2
result = square_of_7()
print(result)  #doesn't print anything because you need to return the value


def square_of_7():
    return 7**2
result = square_of_7()
print(result)

# return (1) exits the function (2) Outputs whatever value is placed after the return keyword (3) Pops the function off of the call stack

def square_of_7():
    print('I am before the return')
    return 7**2
    print('I am after the return') #doesn't get printed
result = square_of_7()
print(result)