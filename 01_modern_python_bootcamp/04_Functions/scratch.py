# def multiply_even_numbers(alist):
#     total = 1
#     for i in alist:
#         print(i)
#         if i % 2 == 0:
#             total *= i
#     return total


# print(multiply_even_numbers([2,3,4,5,6]))


def isEven(num):
    return num % 2 == 0

def partition(a_list, isEven):
    t=[]
    f=[]
    for i in a_list:
        if isEven(i):
            t.append(i)
        else:
            f.append(i)
    return[t,f]

print(partition([1,2,3,4], isEven))

