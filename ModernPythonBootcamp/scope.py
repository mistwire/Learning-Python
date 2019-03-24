# total = 0 #global scope

# def increment():
#     total += 1 #local scope
#     return total #this doesn't work because 'total' in the function isn't assigned, even though total in global scope is 

# increment()


total = 0 #global scope

def increment():
    global total 
    total += 1 #references global scope now
    return total  

print(increment())
