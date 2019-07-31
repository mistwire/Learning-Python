numlist = list()
while True:
    inp = input('Enter a number, type "done" when finished: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)

print('Average: ', average)
