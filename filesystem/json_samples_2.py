import json

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

d1_json = json.dumps(d1, indent=True)

with open('json_data.json', 'w+') as file:
    file.write(d1_json)
    print('Data saved in json_data.json')

