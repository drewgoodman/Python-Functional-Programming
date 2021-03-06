import collections
import time
import multiprocessing
from functools import reduce
from pprint import pprint


if __name__ == '__main__':
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
    pprint(scientists)
    print()

    def transform(x):
        print(f'Processing record {x.name}...')
        time.sleep(1) #simulating more complex operation
        result = {'name': x.name, 'age': 2020 - x.born}
        print(f'Done processing record {x.name}')
        return result

    start = time.time()

    with multiprocessing.Pool() as pool:
        # start = time.time()
        result = pool.map(transform, scientists)

    # result = tuple(map(
    #     transform, scientists
    # ))

    end = time.time()

    print(f'\nTime to completion: {end - start:.3f} seconds\n')
    pprint(result)