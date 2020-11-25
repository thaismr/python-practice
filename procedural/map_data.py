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
    {'name': 'Ble', 'age': 25},
    {'name': 'Bli', 'age': 25},
    {'name': 'Blo', 'age': 25},
    {'name': 'Blu', 'age': 25},
    {'name': 'Jane', 'age': 25},
    {'name': 'John', 'age': 25},
    {'name': 'Doe', 'age': 25},
    {'name': 'Fulano', 'age': 25},
    {'name': 'Beltrano', 'age': 25},
]

my_list = list(range(1, 11))
