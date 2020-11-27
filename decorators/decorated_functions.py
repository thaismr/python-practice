print()


def master(f):
    # Decorate whatever function I get as 'f':
    def slave(*args, **kwargs):
        # add decoration
        print('I am a decoration.')

        # Include the original function as part of me.
        # I don't need to know what my decorated function is or does bellow:
        result = f(*args, **kwargs)

        return result  # in case our f() returned a value

    # Return 'f' decorated:
    return slave


# An undecorated, dull Hello World:
def hello_world():
    print('Hello World...')


# Now let's decorate our Hello World function:
hello_world = master(hello_world)  # Hello World now includes extra code from slave

# Whenever we need to use it now:
print('Calling "Hello World":')
hello_world()


# Have it decorated from start:
@master
def decorated_hello_world(test=None):
    print('Hello World!', test or '')


print()
print('Calling our "Decorated Hello World":')
decorated_hello_world()


# We can include arguments and keyword arguments
# if our SLAVE function gets them and passes them along
print()
print('Calling our "Decorated Hello World":')
decorated_hello_world('Plus some args...')
