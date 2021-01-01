# Play sounds on certain beats on 4/4 time
# create a function that always gives us the current beat - 1,2,3,4,1,2,3,4,1,2,3,4

def current_beat():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1


counter = current_beat()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))