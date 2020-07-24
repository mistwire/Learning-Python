def sum_numbers(numbers=None):
    sum = 0
    if numbers:
        for arg in numbers:
            sum += arg
        return sum
    return sum(range(1,101))


print(sum_numbers())
print(sum_numbers(range(1, 11)))
print(sum_numbers([1, 2, 3]))
print(sum_numbers((1, 2, 3)))
print(sum_numbers([]))

