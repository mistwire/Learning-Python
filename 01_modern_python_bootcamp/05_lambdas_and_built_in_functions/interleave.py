# Staggered over 3 lines:
def interleave(string1, string2):
    first_list = list(zip(string1, string2))
    second_list = list("".join(i) for i in first_list)
    return "".join(second_list)

# All in one list comp:
def interleave2(str1, str2):
    return ''.join(''.join(x) for x in (zip(str1, str2)))

print(interleave("Heya!", "Chris"))

print(interleave2("Hello", "World"))

