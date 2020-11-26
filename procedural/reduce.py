from procedural.map_data import products, people, my_list
from functools import reduce

##
# Reduce:
# Acumula todos os valores de uma lista, e os reduz a um unico item
##
print()


# Understanding how it works:
reduced = 0
for n in my_list:
    reduced += n

print(reduced)  # summed all values in my_list and returned a single result


# Doing the same with REDUCE:

reduced_2 = reduce(lambda f, n: n + f, my_list, 0)

print(reduced_2)  # same result with 1 line of code


# Product prices summed with REDUCE:

delivery = 2000  # start summing from base delivery costs (in cents)

cart_total = reduce(lambda accumulated_total, product: product['price'] + accumulated_total, products, delivery)

print(f'Buy all for ${cart_total/100}')


# Average age of all people in our data file:

ages_sum = reduce(lambda ac, person: person['age'] + ac, people, 0)

print(
    'Average age of people in our data file is {average:.0f} years old, out of {count} individuals.'
    .format(average=ages_sum/len(people), count=len(people))
)
