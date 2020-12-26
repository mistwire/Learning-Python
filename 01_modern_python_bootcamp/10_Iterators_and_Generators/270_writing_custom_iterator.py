# create our own version of range

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    
    # iter needs to return an iterator
    def __iter__(self):
        # return iter("hello")
        return self

    # the __iter__ self needs __next__ defined
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

c = Counter(0,10)
print(iter(c))

for x in Counter(0,10):
    print(x) 