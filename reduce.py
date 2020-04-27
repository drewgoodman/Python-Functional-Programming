import collections
from functools import reduce
from pprint import pprint

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel'
])

scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)


names_and_ages = tuple(map(
    lambda x: {"name":x.name, "age": 2020 - x.born},
    scientists
))

pprint(names_and_ages)

# add all ages accumulatively
total_age = reduce(
    lambda acc, val: acc + val['age'],
    names_and_ages,
    0
)

print(total_age)

# group scientists by field

def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc

scientists_by_field = reduce(
    reducer,
    scientists,
    {'math': [], 'physics' : [], 'chemistry': [], 'astronomy': []}
)

pprint(scientists_by_field)

scientists_by_field_two = reduce(
    reducer, scientists, collections.defaultdict(list)
)

pprint(scientists_by_field_two)

dd = collections.defaultdict(list)
print(dd)
print(dd['doesntexist'])
print(dd)
dd['xyz'].append(7)
dd['xyz'].append(2)
dd['xyz'].append(3)
print(dd)