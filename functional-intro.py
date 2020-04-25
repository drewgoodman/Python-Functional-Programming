# functional programming - avoids bugs by performing computation through evaluating functions -- lots of immutable data

# scientists = [
#     { 'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'noble': False}
# ]

# print(scientists)
# scientists[0]['name'] = "Ed Lovelace"
# print(scientists)

import collections
from pprint import pprint

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel'
])

ada = Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False)
# print(ada.name)
# ada.name = 'Ed Lovelace'
print(ada)

scientistsList = [
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
]

pprint(scientistsList)
del scientistsList[0] # can still delete
pprint(scientistsList)

scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)


pprint(scientists)
print(scientists[0].name)
# del scientists[0]
# pprint(scientists)
