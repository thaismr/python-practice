# #
# Format : Currency
# #

# Format currency as Dollar:

def format_dollar(value):
    if isinstance(value, int):  # if int, convert from cents to dollar first
        value /= 100
    return f'${value:.2f}'


# Format currency as Real:

def format_real(value):
    if isinstance(value, int):  # if int, convert from cents to dollar first
        value /= 100
    return f'R${value:.2f}'.replace('.', ',')


if __name__ == '__main__':
    # debug:
    print(format_dollar(2000))
    print(format_dollar(5.555))
    print(format_real(4444.44))
    print(format_real(500))
