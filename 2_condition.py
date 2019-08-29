b = False
t = 0

# Conditions
# Blocks with indentation (4 spaces PEP8)
if b:
    pass
else:
    print('b is false')



if not b or T:
    print('Lazy evaluation runs - even when T is not exists')



# Object identity caching similar to Java Integer(127)
a = 2
b = 2
if a is b:
    print('a and b is the same object')


# Reassignment again
a = [1, 2]
b = [1, 2]
if a is not b:
    print('a and b not anymore the same')



# Containing
l = [4, 5]
if 5 in l:
    print('5 is in the list', l)



# Ternary is weird in python
b = False
print('Ternary is weird') if not b else print('Ternary is fine')
