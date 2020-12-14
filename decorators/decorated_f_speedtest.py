from time import time, sleep


def speed_test(f):
    def run_with_speed_test(*args, **kwargs):
        start = time()

        # in case our f() returns a value we need to pass along:
        result = f(*args, **kwargs)

        end = time()
        speed = (end - start) * 1000  # x1000 to get result in milliseconds
        print(f'Function {f.__name__} took {speed:.2f}ms to complete')

        # in case our f() returns a value:
        return result

    return run_with_speed_test


@speed_test
def take_some_time(test=None):
    for i in range(10):
        print(i, end=' ')
        sleep(.1)

    print()
    print(test or '')
    print()
    return 'Test decorated function with a return value.'


take_some_time()

print()


# Debug:
test_return = take_some_time('test args')

print(test_return)
