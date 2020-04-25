import collections
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

pprint(filter(lambda x: x.nobel is True, scientists))
# <filter object at 0x000002BA35B2C040>

fs = filter(lambda x: x.nobel is True, scientists)
print(next(fs))
print(next(fs))
print(next(fs))
# print(next(fs))
# StopIteration exception

filtered = tuple(filter(lambda x: x.nobel, scientists))
pprint(filtered)

# pprint(tuple(filter(lambda x: True, scientists))) 
#   Return everything

pprint(tuple(filter(lambda x: x.field == 'physics' and x.nobel, scientists)))
# returns only Marie Curie

def nobel_filter(x):
    return x.nobel is True

pprint(tuple(filter(nobel_filter, scientists)))

# [x for x in scientists if x.nobel is True] - pythonic version of above code
pprint(tuple([x for x in scientists if x.nobel is True]))

# tuple ([1,2,3])
# (1,2,3)

print("Birthday more recent than 1900")
pprint(tuple([x for x in scientists if x.born >= 1900]))