# #
# Try: Except as conditional
# #

def convert_to_number(var):
    try:
        var = int(var)
        return var
    except ValueError:
        try:
            var = float(var)
            return var
        except ValueError:
            pass


while True:
    get_var = input('Please type a number: ')

    num = convert_to_number(get_var)

    if num is not None:
        print(num)
    else:
        print('not a number')
