# **kwargs keyword args
# gather remainind keyword arguments & stores in a dictionary (instead of a tuple for *args)
# can be any name **stuff, **whatever, standard is **kwargs

def fav_colors(**kwargs):
    print(kwargs) #collects all arguments & puts into dictionary
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby="red", ethel="teal")
fav_colors(colt="super duper purple")

def special_greeting(**kwargs):
    if "Chris" in kwargs and kwargs["Chris"] == "special":
        return "You get a special greeting Chris!"
    elif "Chris" in kwargs:
        return f"{kwargs['Chris'].title()} Chris!" #prints titled value of Chris key so hello! becomes Hello!
    return "New phone who dis?"

print(special_greeting(Chris="hello")) # returns Hello Chris!
print(special_greeting(Bob="hello")) # returns New phone who dis?
print(special_greeting(Chris="special")) # returns You get a special greeting Chris!


# kwargs exercise - create a function called combine_words that takes a string & any # of additional arguments.
def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

print(f'\n{combine_words("child")}')
print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))
print(combine_words("work", suffix="er"))
print(combine_words("work", prefix="home"))