def sum_numbers(numbers=None):
    if numbers is None:
        nubmers = range(1,101)
    return sum(numbers)
    
print(sum_numbers(range(1, 11)))
print(sum_numbers([1, 2, 3]))
print(sum_numbers((1, 2, 3)))
print(sum_numbers([]))
print(sum_numbers(None))


