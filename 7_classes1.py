class Person:
    classVar = 'this is a class variable'

    def __init__(self, name):
        # This is an instance variable
        self.name = name
        print('init called')

    # The first implicit parameter is always a reference to the instance and it is called self by convention
    def say(self, something):
        print(f'{self.name} says {something}')

    # The first implicit parameter is always a reference to the class and it is called cls by convention
    @classmethod
    def updateAndPrintStatic(cls, str='other'):
        cls.classVar = str
        print(cls.classVar)

    @staticmethod
    def staticMethod(*args):
        print(f'This function should only work on the {len(args)} input parameters')


bob = Person('bob')

# Same thing
bob.say('hello')
Person.say(bob, 'hello')


input(('\n' * 2) + 'Enter to continue...')
print(Person.classVar)
Person.updateAndPrintStatic()
Person.staticMethod(1, 2, 3, 4, 5)
