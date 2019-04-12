for i in [5,4,3,2,1]:
    print(i)
print ('Blastoff!')

n = 5
while n > 0:
    print (n)
    n = n -1 
print('Blastoff!')
print(n)

friends = ['Joseph','Glen','Sally']
for friend in friends:
    print('Happy New Year:',friend)

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print("After", largest_so_far)

count = 0
sum = 0 
print ('before', count, sum)
for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print (count,sum, value)
print("after", count, sum, sum/count)

#search using a boolean value
found = False
print ("Before", found)
for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
        break
    print(found, value)
print("After", found)

#finding the smallest value
smallest = None
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print ("After", smallest)
