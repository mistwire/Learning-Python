# a list is a collection of items in a particular order

colors = ['blue', 'red', 'indigo', 'violet', 'yellow', 'green', 'orange', 'amber', 'purple']

print(colors[0])  # prints the 1st item in the list
print(colors[3].title()) # prints the 4th item in the list and usues title method to capitalize the 1st letter
print(colors[-1]) # prints the last item in the list

# Changing, Adding, and Removing elements in a list

colors[7] = 'brown' # changes the 8th element ('amber') to 'brown
print(colors)

colors.append('magenta') # adds element to the end of the list
print(colors)

colors.insert(4, 'pink') # adds element to the 4th index position
print(colors)

del colors[-1] #deletes the last item in the list (in this case 'magenta')
# use del when you know the index position of the element you want to delete
print(colors)

# use pop when you still want to work with the removed element:
popped_color = colors.pop() #pops last element, in this case 'purple' 
print(popped_color)
print(colors)

# use remove() method to remove by value:
colors.remove('indigo') # removes 1st instance of an element
print(colors)

# Organizing a list:
# use sort() method to permanently sort a list, use sorted() function to temporarily sort:
print('\nPrinting colors using sorted function')
print(sorted(colors))
colors.sort()
print('\nPrinting colors using sort method with reverse=True')
colors.sort(reverse=True)
print(colors)


# Copying a list:
# use new_list = old_list[:] 
# new_list = old_list doesn't work because they are both referencing the same list
my_foods = ['sushi', 'pizza', 'cheeseburger']
kim_food = my_foods[:]

kim_food.append('ice cream')
my_foods.append('ramen')

print(f'My favorite foods are \n {my_foods}')
print(f"Kim's favorite foods are \n {kim_food}")

# Checking that a list is not empty:
requested_toppings = []
if requested_toppings: # Checks for the truthiness of the list, if empty it is False
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")



# This is a good cheat sheet https://www.learnpython.dev/ 