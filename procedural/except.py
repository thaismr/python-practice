# #
# Try: Except
# Dealing with errors in Python
# #
print()

try:
    # f = []
    # print(f[1])
    a = {}

except NameError as error:  # eg: var not defined
    print('Error:', error)

except (IndexError, KeyError) as error:  # eg: var[i] is out of range or key type error {} /= []
    print('Error:', error)

except Exception as error:  # any other error type
    print('Unexpected error...', error)

else:
    print('Success! All is fine with the code.')
    print(a)  # prints {}

finally:
    print('Finally, here we are, whether code was successful or not.')

print()
print('Code moves along...')

print()


# Sample try/except:

try:
    a = 1/0  # something is wrong here..
except:
    a = None  # we set "a" to None to prevent breaking the code later
else:
    pass  # do nothing here

print(a)


# Try/ except inside try /except:

try:
    a = 0
    try:
        b = 1/a
    except:
        print('Something went wrong with "b"...')
except:
    print('Something went wrong with "a"...')
else:
    print('All went well with "a", even if "b" goes badly!')
