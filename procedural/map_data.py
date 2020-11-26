##
# Data for use in map.py
##

# Generate sample products list:
# Using: round(price/.48, 2) to generate a float (price/.48) and round it to .2f
# Industry standard: store currency as CENTS using INTs, by multiplying actual price * 100.
products = [
    {'name': 'Product #' + str(i), 'price': int(round(price/.48, 2) * 100)}
    for i, price in enumerate(range(30, 40))
]

people = [
    {'name': 'Bla', 'age': 25},
    {'name': 'Ble', 'age': 26},
    {'name': 'Bli', 'age': 27},
    {'name': 'Blo', 'age': 28},
    {'name': 'Blu', 'age': 29},
    {'name': 'Jane', 'age': 35},
    {'name': 'John', 'age': 45},
    {'name': 'Doe', 'age': 55},
    {'name': 'Fulano', 'age': 65},
    {'name': 'Beltrano', 'age': 75},
]

my_list = list(range(1, 11))
