person = {'name': 'Vadim'}

print(person)

person['age'] = 33
print(person)

found = {}

for item in ['a', 'e', 'i', 'o', 'i', 'c']:
    found[item] = 0
print(found)

for key, value in sorted(found.items()):
    print("key:", key, "value:", value)


print("null = ", found.__contains__('a'))


found.setdefault('default', 'defaultValue')
print(found['default'])

people = {}
people['Ford'] = {'Name': 'FordPerfect',
                  'Gender': 'Mane',
                  "HomePlanet": 'Betelgeuse Sever'}
import pprint

pprint.pprint(people)

del people['Ford']
print(people if people else '123')