class Person:
    static = 'this is a static or class variable'

    def __init__(self, name):
        # This is an instance variable
        self.name = name

    # The first implicit parameter is always a reference to the instance and it is called self by convention
    def say(self, something):
        print(f'{self.name} says {something}')

    # The first implicit parameter is always a reference to the class and it is called cls by convention
    @classmethod
    def updateAndPrintStatic(cls, str='other'):
        cls.static = str
        print(cls.static)

    @staticmethod
    def staticMethod(*args):
        print(f'This function should only work on the {len(args)} input parameters')



class Developer(Person):
    def __init__(self, name):
        super().__init__(name)
        # You can hide members with this notation
        self.__secret = 'Coffee'

    def say(self):
        print('Code is life')

    def say(self, **kwargs):
        print('No function overload in python')




dave = Developer('Dave')
print(dave.name)

try:
    print(dave.__secret)
except AttributeError as err:
    print(dave.name, 'keep his secret')
    print('But not from me :)', dave.__dict__)





input(('\n' * 2) + 'Enter to continue...')
dave.say()
dave.say(overload=True)


Developer.ask = lambda self: print('Why no function overload in python?')
dave.ask()
