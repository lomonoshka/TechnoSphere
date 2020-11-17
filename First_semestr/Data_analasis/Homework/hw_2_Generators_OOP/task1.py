def solution1(s):
    return [c * 4 for c in s]


def solution2(s):
    return [c * (i + 1) for i, c in enumerate(s)]


def solution3(a):
    return [i for i in a if i % 3 == 0 or i % 5 == 0]


def solution4(a):
    return [i for sublist in a for i in sublist]


def solution5(n):
    return [(i, j, k) for k in range(5, n+1) for j in range(1, k)
            for i in range(1, j) if i**2 + j**2 == k**2]


def solution6(a):
    return [[i + j for j in a[1]] for i in a[0]]


def solution7(A):
    return [[row[i] for row in A] for i in range(len(A[0]))]


def solution8(a):
    return [[int(i) for i in s.split()] for s in a]


def solution9(a):
    return {chr(ord('a') + i): i**2 for i in a}


def solution10(names):
    return {name.capitalize() for name in names if len(name) > 3}


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
