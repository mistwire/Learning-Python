# Use the file name mbox-short.txt as the file name
count = 0
entries = 0
total = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    atpos = line.find(":")
    sppos = line.find(" ", atpos)
    host = line[atpos+1 : ]
    total = total + float(host)
    count = count + 1
    #print(total/count)
    #print(line)
print("Average spam confidence:", total/count)
