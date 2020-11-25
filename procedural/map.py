from procedural.map_data import my_list

##
# Python Map()
# Runs a given Function through each element of a given Iterable, and returns a resulting Iterator
# map(function, iterable) -> iterator
##

# We take my_list from our map_data, imported on top of this file
list_doubled = map(lambda x: x * 2, my_list)

print(my_list)
print(list(list_doubled))


# We would rarely use the MAP function, instead we can use list COMPREHENSION:
list_doubled_cph = [x * 2 for x in my_list]

print(list_doubled_cph)


# For optimization sake, we can use a GENERATOR instead of a LIST
list_doubled_gen = (x * 2 for x in my_list)

print(list(list_doubled_gen))
