# Explain mem usage in generators using Fibonacci numbers

def fib_list(max):
    nums = []
    a,b = 0,1
    while len(nums) < max:
        nums.append(b)
        a,b = b, a+b
    return nums

print(fib_list(10))


def fib_gen(max):
    x = 0 
    y = 1
    count = 0 # no list with a generator... ?
    while count < max:
        x,y = y, x+y
        yield x
        count += 1

gen = fib_gen(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for n in fib_gen(1_000_000):
    print(n)
# This uses a lot less memory than the list above

