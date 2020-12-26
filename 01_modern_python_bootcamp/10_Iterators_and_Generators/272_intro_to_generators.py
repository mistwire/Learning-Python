# generators are iterators
# not all iterators are generators
# regular functions use return keyword
# generator functions use the yield keyword
# can be created with generator expressions

# our 1st generator
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count +=1 