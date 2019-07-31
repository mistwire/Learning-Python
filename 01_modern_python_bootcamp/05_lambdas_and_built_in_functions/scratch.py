string1 = "ha"
string2 = "hi"

zipped = list(zip(string1, string2))
print(zipped)
["".join(i) for i in zipped]


