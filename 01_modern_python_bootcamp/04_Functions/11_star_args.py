# *args ('star args')

# A special operator we can pass to functions
# Gathers remaining arguments as a tuple
# This is a parameter, can call it whatever I want *args, *nums, *doofus
def sum_all_nums(num1, num2, num3):
    return num1 + num2 + num3
print(sum_all_nums(5, 5, 9)) 

# What if you wanted to pass in ANY number of numbers?

def sum_all_nums(*args):
    print(args) # refer to the parameter withouth the * inside the function
    total = 0 
    for num in args:
        total += num
    return total
print(sum_all_nums(2,3,4)) 
print(sum_all_nums(2, 4, 10, 3, 4)) 

# Another example:

def ensure_correct_info(*args):
    print(args)
    if "Chris" in args and "Williams" in args:
        return "Welcome back Chris!"
    return "New phone who dis?"

print(ensure_correct_info())

print(ensure_correct_info(1, "Williams", ["Bob", 1, False], "Chris", True))