"""
Recommended:
https://rszalski.github.io/magicmethods/
"""


class A:
    def __new__(cls, *args, **kwargs):
        # I am the constructor class
        # Let our super() object class create our object
        print('I am NEW')
        cls.test = 'I am a test argument'

        def say_hi(*args, **kwargs):
            print('Hi!')

        cls.say_hi = say_hi

        return object.__new__(cls)

    def __init__(self):
        print('I am INIT')


a = A()
print(a.test)
a.say_hi()

