from colorama import init
from termcolor import colored
 
# use colorama to make termcolor work on Windows too
init()
 
# then use termcolor for all colored text output
print(colored('Hello, World!', 'green', 'on_red'))