han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    #print('words:', wds)
    if len(wds) < 3 or wds[0] != 'From':  #Guardian pattern
        continue
    '''
    if wds[0] != 'From':
        #print('Ignore')
        continue
    '''
    print(wds[2])

