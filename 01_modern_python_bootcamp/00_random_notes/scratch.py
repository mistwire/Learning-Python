# a_list = [1,2,3,4,10,11]

# def simpleArraySum(ar):
#     total = 0
#     for num in ar:
#         total += num
#     return total

# simpleArraySum(a_list)


# msg="""Dear Terry,,
# You must cut down the mightiest 
# tree in the forest with…
# a herring! <3"""
# print(msg)


# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1


import re 

def validate_pin(pin):
    match4 = re.search(r'\d{4}', pin)
    #match6 = re.search(r'\d{6}', pin)
    if match4: # or match6:
        return True
    return False

print(validate_pin('12345'))