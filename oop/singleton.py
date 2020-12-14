"""
SINGLETON design pattern example
"""


class Singleton:
    # overwriting constructor method:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_myself'):
            cls._myself = object.__new__(cls)

        return cls._myself


a = Singleton()
b = Singleton()

print(a == b)  # both instances are the same object in memory
print(id(a), id(b))
