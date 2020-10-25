from functools import reduce
from itertools import starmap
import re
from operator import itemgetter


def solution1(a):
    return list(map(lambda x: int(re.sub("[^0-9]", "", x[::-1])), a))


def solution2(a):
    return list(starmap(lambda x, y: x * y, a))


def solution3(a):
    return list(filter(lambda x: x % 6 in [0, 2, 5], a))


def solution4(a):
    return list(filter(lambda x: x, a))


def solution5(a):
    list(map(lambda x: x.update({"square": x["width"] * x["length"]}), a))
    return a


def solution6(a):
    return list(map(lambda x: dict([*x.items(), ("square", x["width"] * x["length"])]), a))


def solution7(a):
    return set(reduce(lambda x, y: x & y, a))


def solution8(a):
    d = {}
    list(map(lambda x: d.update({x: 1 if d.get(x) is None else d[x] + 1}), a))
    return d


def solution9(a):
    return list(map(itemgetter('name'), filter(lambda x: x['gpa'] > 4.5, a)))


def solution10(a):
    return list(filter(lambda x: reduce(lambda x, y: -(int(x) - int(y)), x) == 0, a))


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10
}
