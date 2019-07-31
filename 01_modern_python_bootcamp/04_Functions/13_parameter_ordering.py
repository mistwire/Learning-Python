# Parameters HAVE to go in a specific order:
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

def display_info(a,b,*args, instructor="Chris", **kwargs):
    return [a, b, args, instructor, kwargs]

print(display_info(1, 2, 3, last_name="Williams", job="Numbnuts"))

