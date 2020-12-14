class A:
    def __setattr__(self, key, value):
        self.__dict__[key] = value


a = A()
a.test = 'something'

print(a.test, type(a.test))
