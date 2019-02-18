import os
import pprint
from datetime import datetime
import requests
from url_utils import gen_from_urls

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


if os.path.isfile('bussers.csv'):
    with open('bussers.csv') as data:
        ignore = data.readline()
        flights = {}
        for line in data:
            # strip deletes spaces at the start and end of line (\t, \n, \r)
            k, v = line.strip().split(',')
            flights[k.strip()] = v.strip()
    pprint.pprint(flights)
else:
    print('no file, sorry')


flights2 = {}
for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()


pprint.pprint(flights2)


# generators for lists
more_dests = [dest.title() for dest in flights.values()]

print('more_dest  =', more_dests)

# generators fore dictionary
more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}
print('more_flights', more_flights)


just_freeport = {convert2ampm(k): v.title()
                 for k, v in flights.items()
                 if v == 'FREEPORT'}

print('just_freeport', just_freeport)


dests = set(flights.values())
print('dests = ', dests)

for dest in set(flights.values()):
    print(dest, '->', [k for k, v in flights.items() if v == dest])


when = {dest: [k for k, v in flights.items() if v == dest] for dest in set(flights.values())}

print('when =', when)

# set generator
vowels = {'a', 'e', 'i', 'o'}
message = 'Dont forget to pack your towel'

found = set()
for v in vowels:
    if v in message:
        found.add(v)

print('found = ', found)
found2 = { v for v in vowels if v in message}

print('found2 = ', found2)


# ---

urls = ('http://headfirstlabs.com', 'http://twitter.com', 'http://facebook.com')
# generators of lists forece cycle for wait till list is generated [] -> generator of lists
# when list is generated then cycle for is printing data in that list
# for resp in [requests.get(url) for url in urls]:
#     print(len(resp.content), '->', resp.status_code, '->', resp.url)
# expression generator generates values one by one and once he generated first value he passes it into for cycle
# so it is very responsive and make sense when u have a lot of data and cant wait till 100 bilions of data will be
# generated in list


# for resp in (requests.get(url) for url in urls):
#     print(len(resp.content), '->', resp.status_code, '->', resp.url)


for resp_len, status, url, in gen_from_urls(urls):
    print(resp_len, status, url)