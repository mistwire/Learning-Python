# aggregates elements from each of the iterables
# returns an iterator of tuples
# stops when the shortest input is exhausted


print(zip([1,2,3], ["a", "b", "c"]))

first_zip = zip([1,2,3], ["a", "b", "c"])
print(list(first_zip))
first_zip = zip([1,2,3], ["a", "b", "c"]) #have to re-run the zip to get the zip object back
print(dict(first_zip))

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]

print(dict(zip(nums1, nums2)))

words = ['hi', 'lol', ':-)', 'hahaha']

print(list(zip(words, nums1, nums2)))

# using * to unpack tuples:

five_by_two = [(0,'a'), (1,'b'), (2,'c'), (3, 'd'), (4, 'e')]

print(list(zip(*five_by_two)))


# more complex zip examples:
# 3 lists:
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']
# Make a structure that looks like this: {'dan': 98, 'ang': 91, 'kate': 78}
# Throw out lowest score & avg the two others 

# with Dict comprehension:
final_grades = [pair for pair in zip(midterms, finals)]
print(final_grades)

# now find max
final_grades = [max(pair) for pair in zip(midterms, finals)]
print(final_grades)

# now turn it into a dict & add student name:
final_grades = {pair[0]:max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}
print(final_grades)

# now with a lambda and map
