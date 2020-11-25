from procedural.map_data import products

##
# Python Map()
# Runs a given Function through each element of a given Iterable, and returns a resulting Iterator
# map(function, iterable) -> iterator
##

# Map products' prices as float/dollars (by dividing /100):
# (using a LAMBDA function PRESERVES our original list)
map_prices = map(lambda prod: prod['price'] / 100, products)

print(list(map_prices))

# Original list was unaffected:
print(products)
print()


# Using a named function to convert our prices from int/cents to float/dollars:
def price_to_dollar(prod):
    prod['price'] /= 100
    return prod


products_to_dollar = map(price_to_dollar, products)  # Creates our ITERATOR

# Our SOURCE products (ORIGINAL):
print(products)

# Using a NAMED FUNCTION inside MAP will affect our ORIGINAL list as we go through our mapped ITERATOR:
print(list(products_to_dollar))

# Our iterator is now empty:
print(list(products_to_dollar))  # []

# Our SOURCE products now CHANGED:
print(products)

print()
print()

##
# COMPARISON:
# Doing the same with dictionary comprehension
##

# Getting prices back as int/dollars:
get_prices_cph = [int(product['price'] * 100) for product in products]

print(get_prices_cph)
print(products)  # our source is unaffected
print()


# Using a NAMED function with comprehension (will now AFFECT ORIGINAL):
def price_to_cents(prod):
    prod['price'] = int(prod['price'] * 100)
    return prod


products_to_cents = [price_to_cents(product) for product in products]

print(products_to_cents)
print(products)  # our source is now back to cents/int

