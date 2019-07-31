'''
Take the following Python code that stores a string:`
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
Exercise 6:
Read the documentation of the string methods at
https://docs.python.org/3.5/library/stdtypes.html#string-methods
You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.
The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.
'''

data = 'X-DSPAM-Confidence:0.8475'
atpos = data.find(":")
#print(atpos)
sppos = data.find(" ", atpos)
#print(sppos)
host = data[atpos+1 : ]
print(float(host))

