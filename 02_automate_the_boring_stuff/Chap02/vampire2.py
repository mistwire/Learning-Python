if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000: #this option will never run because 2nd elif takes precedent.
    print('Unlike you, Alice is not an undead, immortal vampire.')

