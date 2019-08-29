l1 = [1, 'a', 5]
print(l1)

# Feel free to use comma after the last entry
l2 = [
    [1, 2],
    [2, 3],
]

print(l2)
















input(('\n' * 2) + 'Enter to continue...')
# Range to list
print(list(range(6)))


# Tuple to list
print(list((3, 4, 5)))


















input(('\n' * 2) + 'Enter to continue...')
list1 = [x + 2 for x in (range(6))]
print('Original list:', list1)

# Some more syntax sugar [start:stop:step]
print('Without the first', list1[1:])
print('Without the last', list1[:-1])
print('Reversed list', list1[::-1])
print('Every even index', list1[::2])

print('Sort evens and odds', list1[::2] + list1[1::2])
