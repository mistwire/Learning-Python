# try:
# except:
# else:
# finally:

while True:
    try:
        num = int(input("Please enter a number: "))
    except ValueError:
        print("That's not a number")
    else:
        print("I'm in the else!") # doesn't run if except runs
        break
    finally:
        print("Runs no matter what!") # runs no matter what



