"""For this exercise you can assume numerator and denominator are of type
int/str/float. Try to convert numerator and denominator to int types, if that raises a
ValueError reraise it. Following do the division and return the result.
However if denominator is 0 catch the corresponding exception Python
throws (cannot divide by 0), and return 0"""




# def divide_numbers(numerator, denominator):
#     try:
#         int_numerator = int(numerator)
 
#        int_denominator = int(denominator)
#     except ValueError:
#         if numerator or denominator == str:
#             raise ValueError("Cannot be a string!")
#     try:
#         result = int_numerator/int_denominator
#     except ZeroDivisionError:
#         if int_denominator == 0:
#             return 0
#     return result

def divide_numbers(numerator, denominator):
    try:
        return int(numerator)/int(denominator)
    except ValueError:
        raise
    except ZeroDivisionError:
        return 0






print(divide_numbers(10,5))
print(divide_numbers('hi',5))
