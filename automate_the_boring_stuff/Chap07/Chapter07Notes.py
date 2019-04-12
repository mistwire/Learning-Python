# All regex functions are in the "re" module
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #re.compile creates the regex object
mo = phoneNumRegex.search('My number is 123-456-7890') # mo is the 'Match object' which matches the regex search pattern
print('Phone number found: ' + mo.group()) #prints the match object group (0)


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') 
mo = phoneNumRegex.search('My number is 405-555-7890')
print(mo.group(0)) 
print(mo.group(1))
print(mo.group(2))
print(mo.groups()) # Note the plural form 'groups'
areaCode, mainNumber = mo.groups() # since mo.groups() returns a tuple of multiple values, you can use the multi-value assignment trick to assign each value to a separate variable
print(areaCode)
print(mainNumber)

#groups with items that need parenthesis:
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (405) 555-7890')
print(mo.group(0)) 
print(mo.group(1))
print(mo.group(2))

#matching multiple groups with the Pipe | 
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group()) #Prints the 1st thing it finds

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group()) #Prints the 1st thing it finds

mo2 = heroRegex.findall('Tina Fey and Batman')
print(mo2) #when you use the findall method it grabs all objects

#Use pipe to match one of several patterns:
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search("Batman's Batmobile lost a wheel")
print(mo.group()) #will print out 'Batman' but not 'Batmobile'










