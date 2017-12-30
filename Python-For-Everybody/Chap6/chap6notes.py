#Strings

fruit = 'banana'
letter = fruit[1]
print(letter)

#print the length of the fruit string
print(len(fruit))

#looping through a string
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#or (a "better" way if you don't need to know the index #)
for letter in fruit:
    print(letter)

#count all of a certain letter in a sting
word = 'Banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

#slicing strings
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

#string concatenation
a = "Hello"
b = a + "There"
print(b)
print(a,b)

#Using in as a logical Operator - using in to check if one string is 'in' another string
print('n' in fruit)
print('m' in fruit)
if 'a' in fruit:
    print("I found an 'a'!")

#string comparison
if word.lower() == 'banana':
    print("all right, bananas")
if word < 'banana':
    print("Your word, " + word + ', comes before banana.')
if word > 'banana':
    print("Your word, " + word + ', comes after banana.')

#string library 
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print(len(greet))
print(greet.lower())
print("Hi Chris!".lower())

stuff="Hello World"
print(stuff)
type(stuff)
dir(stuff)
'''
str.capitalize()
str.center()
str.endswith()
str.find()
str.lstrip()
str.replace()
str.lower()
str.rstrip()
str.strip()
str.upper()
'''
#print the location of 'na' in the string 'banana':
position = fruit.find('na')
aa = fruit.find('z')
print(position)
#returns -1 if find can't find the substring:
print(aa)

#make everything UPPER CASE
greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)
#greet varible doesn't change
www = greet.lower()
print(www)

#Search & Replace
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)
nstr = greet.replace('o', 'X')
print(nstr)

#Stripping whitespace (includes spaces, tabs, new lines)
greet = '    Hello Bob  '
print(greet.rstrip(),greet.lstrip(),greet.strip())

#prefixes (returns T or F)
line = "Please have a nice day"
print(line.startswith("Please"))
print(line.startswith('p'))

#Parsing and extracting
data = "From stephen.marquard@uct.ac.za Sat Jan 5  09:14:16 2008"
#get the position of the 1st @ symbol:
atpos = data.find("@")
print(atpos)
#starting from @ sign position, continue looking for the next space:
sppos = data.find(" ", atpos)
#                       ^ shows where to start find
print(sppos)
host = data[atpos+1 : sppos]
#                      ^ up to but not including
print(host)






