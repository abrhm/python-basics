# Definition
a = {
    1: 'test'
}

print(a[1])

# Append
a[2] = 'yeah'
# Or
a.update({2: 'yeah'})
print(a[2])











input(('\n' * 2) + 'Enter to continue...')
# Iterations
for key in a.keys():
    print('key:', key)

for value in a.values():
    print('value:', value)

for key, value in a.items():
    print('item:', (key, value))














input(('\n' * 2) + 'Enter to continue...')
# Dict from tuples
d1 = dict(
    (
        (1, 'a'),
        (2, 'b'),
    )
)
print('From tuples', d1)



# Dict from lists with zip function
a = [1, 2, 3]
b = [10, 20, 30]
d2 = dict(zip(a, b))
print('From lists with zip', d2)


print('key "1" in d1', 1 in d2)
print('value "10" in d1', 10 in d2.values())


















input(('\n' * 2) + 'Enter to continue...')
print('Get with default', d2.get(4, 0))


# Merge dictionaries similar to JS
x = {
    1: 1,
    2: 2,
}

y = {
    2: 3,
    3: 3,
}
merged = {**x, **y}
print(merged)
