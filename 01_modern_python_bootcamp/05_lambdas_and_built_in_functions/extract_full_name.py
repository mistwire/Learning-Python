
# with map and lambdas
def extract_full_name(names):
    return list(map(lambda x: x['first'] + ' ' + x['last'], names))



# with list comprehension:
def extract_full_name2(l):
    return [x['first'] + ' ' + x['last'] for x in l] 
        

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))


print(extract_full_name2(names)) # ['Elie Schoppik', 'Colt Steele']