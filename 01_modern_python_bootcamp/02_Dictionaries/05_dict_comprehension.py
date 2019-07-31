# the syntax -          {___:___ for ___ in ___}

numbers = dict(first=1, second=2, third=3)

squared_numbers = {key:value**2 for key,value in numbers.items()}

print(squared_numbers)


# another example
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}

print(combo)


#count all the letters in a string and return it as a dictionary:
def multiple_letter_count(a_string):
    return {letter:a_string.count(letter) for letter in a_string}
    pass

print(multiple_letter_count("chrisovalandis"))


def list_manipulation(a_list, command, location, value=None):
    if command == 'remove' and location == 'end':
        return a_list.pop()
    elif command == 'remove' and location == 'beginning':
        return a_list.pop(0)
    elif command == 'add' and location == 'beginning':
        a_list.insert(0, value)
        return a_list
    elif command == 'add' and location == 'end':
        a_list.append(value)
        return a_list
    pass