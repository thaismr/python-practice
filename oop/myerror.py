# ALL we need to create our own Error type:
# Make sure CLASS NAME ends with Error
class MyError(Exception):
    pass


# For use with our Rectangle class:
class RectComparisonError(Exception):
    pass


if __name__ == '__main__':

    # Test function:
    def test_error():
        raise MyError('My new error!')  # raise an error of type MyError


    # Try usage:
    try:
        test_error()
    except MyError as error:
        print(f'Error: {error}')


