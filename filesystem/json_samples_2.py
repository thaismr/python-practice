import json

print()

d1 = {
        'Person 1': {
            'name': 'Someone',
            'age': 33
        },
        'Person 2': {
            'name': 'Someone Else',
            'age': 34
        }
    }

# convert dictionary to JSON
d1_json = json.dumps(d1, indent=True)

# save formatted json as file
with open('json_data.json', 'w+') as file:
    file.write(d1_json)
    print('Data saved in json_data.json')

print()

# get file contents back as dictionary
with open('json_data.json', 'r') as datafile:
    saved_d1 = datafile.read()
    saved_d1 = json.loads(saved_d1)
    print(saved_d1)
    print()

    # we can manipulate data as dictionary now
    for person in saved_d1.values():
        print(person['name'], person['age'])

    print()

    # another format:
    for key, value in saved_d1.items():
        print(key, value)

    print()

    # Or yet:
    for person, data in saved_d1.items():
        print(person)
        print('{} is {} years old.'.format(data['name'], data['age']))

    print()

    # Or yet:
    for person, data in saved_d1.items():
        print(person.upper())
        for key, value in data.items():
            print(f'{key.upper()}: {value}')

