from procedural.map_data import people, my_list

##
# Python filter()
# Runs a given Function through a given Iterable, returning an Iterator with only filtered values
##

greater_than_5 = filter(lambda x: x > 5, my_list)

print(list(greater_than_5))

# COMPREHENSION / GENERATOR for comparison:

greater_than_5_gen = (x for x in my_list if x > 5)

for n in greater_than_5_gen:
    print(n, end=' ')
print()

print()

# FILTER people by age:
elderly_people = filter(lambda p: p['age'] >= 65, people)

for person in elderly_people:
    print(
        '{name} is an {age} years old elder.'
        .format(name=person['name'], age=person['age'])
    )

print()


# FILTER with a named function:
def is_elderly(p): return True if p['age'] >= 65 else False


elderly_people = filter(is_elderly, people)

for person in elderly_people:
    print(
        '{name} is an {age} years old elder.'.format(name=person['name'], age=person['age'])
    )
