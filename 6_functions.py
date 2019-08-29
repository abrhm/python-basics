def div(a, b):
    return a / b

print(div(6, 3))

# Language supporting keyword arguments
print(div(b=6, a=3))










input(('\n' * 2) + 'Enter to continue...')
# Just for the example write a sum function instead of sum()
# For simplicity variables either function or global scoped
def summary(*args):
    s = 0
    for arg in args:
        s += arg
    return s

print(summary(1, 2, 3))












input(('\n' * 2) + 'Enter to continue...')
def kwNames(**kwargs):
    for key in kwargs.keys():
        print(key)

kwNames(well=1, done=2)










input(('\n' * 2) + 'Enter to continue...')
# Example function in python
def superSum(a=1, b=2, *args, **kwargs):
    numbers = [a, b, *args, *kwargs.values()]
    summary = sum(numbers)
    numbersStr = ' + '.join(str(n) for n in numbers)
    print(f'{numbersStr} = {str(summary)}')
    return summary


superSum()
superSum(b=4)
superSum(a=0, test=7, yolo=10)











input(('\n' * 2) + 'Enter to continue...')
# Lambda
increase = lambda x: x + 1
print('Lambda example', increase(6))
















input(('\n' * 2) + 'Enter to continue...')
# Just like in JS fundamental values passed by value AVOID THIS pattern!
def passArgumentByValue(a):
    a += 1
    return a

a = 2
passArgumentByValue(a)
print('Passing basic types by value', a)














input(('\n' * 2) + 'Enter to continue...')
# Just like in JS collections and objects passed by ref AVOID THIS pattern!
def passArgumentByRef(a):
    a.append(200)
    return a

a = [2]
passArgumentByRef(a)
print('Passing collections by ref', a)
