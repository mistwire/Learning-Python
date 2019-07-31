num = 0
tot = 0.0
while True:
    sval = input("Please enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("Invalid Input")
        #continue means "go back up to the top of the loop"
        continue
    num = num + 1
    tot = tot + fval
    #print (tot, num, tot/num)

#print("All Done")
print(tot, num, tot/num)
    
