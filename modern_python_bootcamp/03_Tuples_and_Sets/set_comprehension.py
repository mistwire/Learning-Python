#same as list and dictionary comprehension

print({x**2 for x in range(10)})  # a set comprehension that prints an unordered set of numbers 0-9 squared

print({x:x**2 for x in range(10)}) # by adding a "key:"", it turns into a dictionary comprehension!

print({char.upper() for char in 'chrisovalandis frederick williams'}) # print all unique letters in my name, unordered

my_name = 'chrisovalandis frederick williams'

print({char for char in my_name if char in 'aeiou'}) #prints a set of all the vowels in my name
