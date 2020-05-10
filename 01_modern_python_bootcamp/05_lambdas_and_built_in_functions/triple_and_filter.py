def triple_and_filter(a_list):
    return list(filter(lambda x: x%4 == 0, [x*3 for x in a_list]))



print(triple_and_filter([1,2,3,4])) # [12]
print(triple_and_filter([6,8,10,12])) # [24,36]