# #
# Raise
# Re-raises the last exception
# #
print()


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as e:
        print('Log:', e)  # Let's say we would use the except for our log
        raise  # make sure the next dev can also raise an except


# Someone else comes and uses my 'divide' function:
try:
    print(divide(2, 0))  # division results in 0 and would print 'None' if no exception is raised

    # without the use of "raise" on my code, next developer would not have ZeroDivisionError available here:
except ZeroDivisionError as error:
    print('Someone else got the error from outside my code..:', error)


# Sample handling code exception with RAISE:

def my_own_division(num1, num2):
    if num2 == 0:
        raise ValueError("num2 can't be 0.")  # Raise my own exception, will include traceback function

    return num1 / num2


print(my_own_division(5, 0))
