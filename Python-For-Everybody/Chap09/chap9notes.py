#Dictionaries - a 'bag of values, each with it's own label (key/value pairs)
#List - a linear collection of values that stay in order

purse = dict()
purse['money'] = 12     #money is the key, 12 is the value
purse['candy'] = 3      
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)    

ddd=dict()
ddd['age']=21
ddd['course']=182
print(ddd)
ddd['age'] = 23
print(ddd)

#dictionary literals (Constants) - use curly braces and have a list of key:value pairs
#you can make an empty dictionary using empty curly braces
jjj={'chuck':1,'fred':42,'jan':100}
print(jjj)
ooo={}
print(ooo) 

#basic dictionary counting:
ccc=dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] += 1
print(ccc)

#it is an error to ref a key that doesn't exist in the dict
#we can use the in operator to see if a key is in the dict
print('williams' in ccc)

#when we see a new name, add a new entry in the dict, if 2nd or later time - add to count of name in dict
counts = dict()
names = ['csev', 'cwen', 'csev', 'zquain', 'cwen']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name] += 1
print(counts)

#the get method for dictionaries - checks to see if a key is already present - does all of the things the for loop above does for us
x=counts.get(name,0) #name = key & 0 = default value

counts = dict()
names = ['csev', 'cwen', 'csev', 'zquain', 'cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)

#counting pattern (see wordcount.py)

#definite loops and dictionaries:
counts1 = {'chuck':1,'fred':42,'jan':100}
for key in counts1:
    print(key, counts1[key])

#Retrieving lists of Keys and Values:
print(jjj)
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())  #3 item list which contains "tuples"

#Bonus: Two Iteration Variables!!
print(jjj)
for aaa,bbb in jjj.items(): #two iteration variables here (aaa and bbb)
    print(aaa,bbb)

