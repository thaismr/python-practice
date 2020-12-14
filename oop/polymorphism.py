"""
POLYMORPHISM: Classes inherited from the same superclass
can have methods with the same signature but different behaviors.
Same SIGNATURE = Same quantity and type of parameters.
"""
# import "abc" from Python
from abc import ABC, abstractmethod

print()


class AbstractHello(ABC):
    @abstractmethod
    def hello(self, times=5):
        pass


class HelloWorld(AbstractHello):
    def __init__(self):
        self.extra = 'extra from world'

    def hello(self, times=4):
        print(self.__class__)
        print('Hello, world! ' * times)


class HelloPeople(AbstractHello):
    def __init__(self):
        self.extra = 'exra from people'

    def hello(self, times=3):
        print(self.__class__)
        print(self.extra)
        print('Hello, people. ' * times)


say = HelloWorld()
say.hello()
print()


hello = AbstractHello
world = HelloWorld()
people = HelloPeople      # not executing, just define as type HELLOPEOPLE

people.hello(world)       # sending HELLOWORLD class as SELF instead


print()
