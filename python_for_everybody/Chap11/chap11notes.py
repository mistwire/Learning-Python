# Regular Expressions
# http://en.wikipedia.org/wiki/Regular_expressions

'''
^       Matches the beginning of a line
$       Matches the end of a line
?       Optional match ex. 
.       Matches any character
\s      Matches whitespace
\S      Matches any non-whitespace character
*       Repeats a character zero or more times
*?      Repeats a character zero or more times (non-greedy)
+       Repeats a character one or more times
+?      Repeats a character one or more times (non-greedy)
[aeiou] Matches a single character in the listed set
[^XYZ]  Matches a single character NOT in the listed set
[a-z0-9]The set of characters can include a range
(       Indicates where the string extraction is to start
)       Indicates where the string extraction is to end  '''

# must import regex into your program using "import re"
# you can use re.search() , similar to using find()
# you can use re.findall() to extract portions of a string that match your regex, similar to a combination of find() and slicing: var[5:10]

import re

