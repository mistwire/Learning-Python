# The break statement will completely break out of the current loop, meaning it won’t run any more of the statements contained inside of it.
names = ["Max", "Rose", "Nina", "Chris"]
for name in names:
    print(f"Hello, {name}")
    if name == "Nina":
        break # Chris doesn't print


# continue works a little differently. Instead, it goes back to the start of the loop, 
# skipping over any other statements contained within the loop after the continue.
for name in names:
    if name != "Chris":
        continue
    print(f"\nHello, {name}") # only prints out Hello, Chris


count = 0
while True:
    count += 1
    if count == 5:
        print("Count was reached")
        break
        print("This will never print")



