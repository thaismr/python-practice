print()


class A:
    # should instead be an abstract method
    def hello(self):
        # Parent class might have access to children classes
        # The problem is, instance must be a type of child class, not parent
        self.b_hello()


class B(A):
    def b_hello(self):
        print('Hello, World!')


b = B()     # B inherits from A
b.hello()   # I can call A methods (parent) from B (child)

print()


# Using TYPE() to define a new CLASS:
C = type('C', (), {'attr': 1, 'attr_2': 2})

c = C()
print(c.attr)

c.var = 'testing...'
print(c.var)
print(type(c))

# Inheriting from C:
D = type('D', (C,), {'attr_2': 'two'})

d = D()
print(d.attr, d.attr_2)
