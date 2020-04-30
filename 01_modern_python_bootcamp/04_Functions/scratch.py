def multiply_even_numbers(alist):
    total = 1
    for i in alist:
        print(i)
        if i % 2 == 0:
            total *= i
    return total


print(multiply_even_numbers([2,3,4,5,6]))