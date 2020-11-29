"""
__CALL__ - Magic Method
Let's your class instance be called as a function
"""
print()


class A:
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)


a = A()  # instantiate

a(1, 2, 3, test='something')  # Will execute __call__


class B:
    def __call__(self, *args, **kwargs):
        plus = []
        for i in args:
            plus.append(i + 1)

        kwargs['test'] += ' else'

        return plus, kwargs


b = B()  # instantiate

result = b(1, 2, 3, test='something')  # Will execute __call__

print()
print(result)
