from functools import reduce
from itertools import tee


def take_obj(obj):
    for item in obj:
        yield item


def loop(objects):
    i = 0
    size = len(objects)
    while True:
        yield i % size, objects[i % size]
        i += 1


def chain_loop(objects):
    generators = [take_obj(obj) for obj in objects]
    empty = set()
    for i, gen in loop(generators):
        if len(empty) == len(objects):
            break
        if i not in empty:
            try:
                yield next(gen)
            except(StopIteration):
                empty.add(i)
