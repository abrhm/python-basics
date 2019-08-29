i = 3
while (i):
    i -= 1
    print(i)















input(('\n' * 2) + 'Enter to continue...')
# With a little bit of range range(from, to, step)
for i in range(2, -1, -1):
    print(i)

















input(('\n' * 2) + 'Enter to continue...')
# With some inlining
for i in reversed(range(3)): text = 'Countdown: ' + str(i); print(text)













input(('\n' * 2) + 'Enter to continue...')
# Print out the odd numbers between 1-7
for x in range(10):
    if not (x % 2):     # Continue if even
        continue

    if x > 7:   # Break if > 7
        break

    print('Next odd number: ' + str(x))

















input(('\n' * 2) + 'Enter to continue...')
# Or in a short form with string interpolation
for x in range(1, 8, 2):
    print(f'Next: {x}')
