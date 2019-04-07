'''
What is a function?
A process for executing a task
It can accept input and return output
print() is a function
.append() is a function that has to have an argument
'''

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']
print(colors)
colors.append('violet')
print(colors)

'''
Why use functions?  
Stay DRY - Don't Repeat Yourself
"Abstract away" code for other users
organizes your code (not spaghetti code)

starts with 'def'
def name_of_function(): 
    stuff to do
'''

def sing_happy_birthday():
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print("Happy Birthday Dear You")
    print("Happy Birthday To You")

sing_happy_birthday()

