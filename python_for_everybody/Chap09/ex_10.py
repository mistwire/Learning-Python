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

#x = di.items()
'''x=sorted(di.items())
print(x) #print all key,value pairs
print(x[:5]) #print top 5 k,v pairs'''

tmp = list()
for k,v in di.items():
    #print(k,v)
    newtup = (v,k)
    tmp.append(newtup)

#print('Flipped', tmp)
tmp = sorted(tmp, reverse=True)
#print ('Sorted', tmp)
#print ('Sorted top 5', tmp[:5])

for v,k in tmp[:5]:
    print(k,v)

