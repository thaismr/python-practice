from procedural.map_data import products
##
# Python Map()
# Runs a given Function through each element of a given Iterable, and returns a resulting Iterator
# map(function, iterable) -> iterator
##

# Map products' prices:
map_prices = map(lambda prod: prod['price'], products)

for price in map_prices:
    print(price/100)
