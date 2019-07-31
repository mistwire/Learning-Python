#set variables as "none" type
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break

    #this is where str will break, set try/except
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    
    if largest is None:
        largest = num
    elif fnum > largest:
        largest = num
    if smallest is None:
        smallest = num
    elif fnum < smallest:
        smallest = num
    print(largest, smallest)


print("Maximum is", largest)
print("Minimum is", smallest)