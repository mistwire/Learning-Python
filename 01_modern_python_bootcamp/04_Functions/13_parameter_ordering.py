# Parameters HAVE to go in a specific order:
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

def display_info(a,b,*args, instructor="Chrisovalandis", **kwargs):
    return [a, b, args, instructor, kwargs]

print(display_info(1, 2, 3, 4, 5, 6, last_name="Williams", job='wannabe programmer :-)'))

# returns [1, 2, (3, 4, 5, 6), 'Chrisovalandis', {'last_name': 'Williams', 'job': 'Numbnuts', 'vocation': 'programmer :-)'}]
#          a  b      *args        keyword arg                               **kwargs 


