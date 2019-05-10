# The break statement will completely break out of the current loop, meaning it won’t run any more of the statements contained inside of it.
names = ["Max", "Rose", "Nina", "Chris"]
for name in names:
    print(f"Hello, {name}")
    if name == "Nina":
        break # Chris doesn't print


