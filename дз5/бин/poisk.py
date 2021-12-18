d = [1, 2, 3, 4, 5, 6, 7]


def poisk(d, n):
    lower = -1
    upper = len(d) - 1
    while lower < upper - 1:
        center = (lower + upper) // 2
        if d[center] >= n:
            upper = center
        else:
            lower = center
    if upper <= lower:
        return None
    elif d[upper] == n:
        return upper


n = int(input("Элемент, который необходимо обнаружить: "))
print(poisk(d, n))
assert poisk([1, 2, 3, 4, 5, 6, 7], 5) == 4
assert poisk([7, 22, 34, 41, 69, 75, 77], 7) == 0
assert poisk([5, 42, 55, 77, 634, 2345, 33245], 1) is None
assert poisk([], 1) is None
assert poisk([1, 1, 1], 1) == 0
assert poisk([], 42) is None
assert poisk([0], 0) == 0
assert poisk([0], 1) is None
assert poisk([-1, 0, 42], 0) == 1
assert poisk([-42, 0, 42], 42) == 2
assert poisk([-6, -5, -4, -3, -2, -1], -4) == 2
assert poisk([1, 2, 3, 4, 5, 6], 4) == 3
assert poisk([1, 2, 3, 4, 5, 6, 7], 4) == 3
assert poisk([1, 2, 3, 4, 5], 7) is None
assert poisk([1, 2, 3, 4, 5, 6], 7) is None
assert poisk([42, 42, 42, 42, 42], 42) == 0
assert poisk([-42, -42, -42, -42, -42], -42) == 0
assert poisk([42, 42, 42, 42, 43], 43) == 4
assert poisk([41, 42, 42, 42, 42], 41) == 0
assert poisk([-2, -2, -1, 0, 1, 2, 2, 2], -1) == 2
assert poisk([-2, -2, -1, 0, 1, 1, 2, 2], 1) == 4