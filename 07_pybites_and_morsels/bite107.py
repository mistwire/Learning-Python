
'''Complete the function below that receives a list of numbers and returns only the even numbers that are > 0 and even (divisible by 2).

The challenge here is to use Python's elegant list comprehension feature to return this with one line of code (while writing readable code).''' 

def filter_positive_even_numbers(numbers):
    return[i for i in numbers if i % 2 == 0 if i > 0]


numbers = list(range(-10, 11))

print(filter_positive_even_numbers(numbers))

print(filter_positive_even_numbers([2, 4, 51, 44, 47, 10]))
