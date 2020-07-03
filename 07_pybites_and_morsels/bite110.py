"""For this exercise you can assume numerator and denominator are of type
int/str/float. Try to convert numerator and denominator to int types, if that raises a
ValueError reraise it. Following do the division and return the result.
However if denominator is 0 catch the corresponding exception Python
throws (cannot divide by 0), and return 0"""




def divide_numbers(numerator, denominator):
    try:
        int(numerator)
    except TypeError as err:
        print(err)
    try:
        int(denominator)
    except TypeError as err:
        print(err)

    return numerator / denominator



print(divide_numbers(10,5))
print(divide_numbers('1',5))
