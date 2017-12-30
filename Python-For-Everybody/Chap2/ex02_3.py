hours = float(input('enter hours:'))
rate = float(input('enter rate:'))
if hours > 40:
    extra = (hours - 40) + (rate * 1.5)
print ("pay:", hours * rate + extra)
