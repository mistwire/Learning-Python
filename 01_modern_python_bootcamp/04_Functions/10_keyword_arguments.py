#different from default parameters
#When you define a function and use = you are setting a default parameter
#When you invoke a function and use = you are making a keyword argument


def full_name(first, last):
    return f"Your name is {first} {last}"



print(full_name(first='Chris', last='Williams'))
print(full_name(last='Williams', first='Chris'))


