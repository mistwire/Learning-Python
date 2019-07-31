fname = input("Enter file: ")
if len(fname) < 1 : fname = "clown.txt"
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)    
    for w in wds:
        #idiom - retrieve/create/update counter
        di[w] = di.get(w, 0) + 1
#print(di)

#now we want to find the most common word:
largest = -1
theword = None
for k,v in di.items():
    # print(k,v)
    if v > largest:
        largest = v
        theword = k #capture, remember the key that was largest

print('Done', theword, largest)