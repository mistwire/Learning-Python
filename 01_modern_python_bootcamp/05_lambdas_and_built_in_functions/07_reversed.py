# Return a reverse iterator (works with more than just list, which is what reverse does)

nums = [1,2,3,4]
print(nums)
nums.reverse() # lists use reverse
print(nums)

# strings and other iterators use reversed:
print(reversed("hello")) # returns a reverse iterator object

for char in reversed("hello world"):
    print(char)

