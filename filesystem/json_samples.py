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

d1_as_json = json.dumps(d1)

d1_indented = json.dumps(d1, indent=True)

print(d1)
print(d1_as_json)

print()
print(d1_indented)
