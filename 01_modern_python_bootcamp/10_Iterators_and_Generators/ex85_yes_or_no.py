def yes_or_no():
    response = "yes"
    while True:
        yield response
        response = "no" if response == "yes" else "yes"

yo = yes_or_no()

print(next(yo))
print(next(yo))
print(next(yo))
print(next(yo))
print(next(yo))
print(next(yo))