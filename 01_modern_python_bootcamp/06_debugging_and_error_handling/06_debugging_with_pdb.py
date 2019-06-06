import pdb

# # pdb.set_trace() is the magic command :-) 
# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)

first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)
