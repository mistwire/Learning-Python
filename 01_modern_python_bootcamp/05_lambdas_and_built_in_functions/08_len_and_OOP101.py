# len returns the length (the number of items) of an object
# The arg can be a sequence (string, tuple, list, range) 
# or a collection (dict, set)

# Here we are creating our own class that returns len as 50 no matter what
class SpecialList:
    def __init__(self, data):
        self.__data = data

    def __len__(self):
        return 50

l1 = SpecialList([1,40,30,100])
l2 = SpecialList([])
print(len(l1))
print(len(l2))


class SpecialList:
    def __init__(self, data):
        self.__data = data

    def __len__(self):
        return self.__data.__len__() // 2 #returns len of list integer divided by 2

l1 = SpecialList([1,40,30,100,1,2,3,4,5,6,7,8,9,0])
l2 = SpecialList([1,2,3,4,5,6,7,8,9])
print(len(l1))
print(len(l2))
