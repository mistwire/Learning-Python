
def week():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        yield day 

testrun = week()
print(next(testrun))

