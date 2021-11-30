d = [1, 2, 3, 4, 5, 6, 7]


def poisk(d, n):
    d = sorted(d)
    lower = 0
    upper = len(d) - 1
    while lower <= upper:
        center = (lower + upper) // 2
        if d[center] == n:
            for m in range(center+1):
                if d[m] == d[center] and m < center:
                    center = m
            return center
        elif d[center] > n:
            upper = center - 1
        elif d[center] < n:
            lower = center + 1
    return None


n = int(input("Элемент, который необходимо обнаружить: "))
print(poisk(d, n))
assert poisk([1, 2, 3, 4, 5, 6, 7], 5) == 4
assert poisk([7, 22, 34, 41, 69, 75, 77], 7) == 0
assert poisk([5, 42, 55, 77, 634, 2345, 33245], 1) is None
assert poisk([], 1) is None
assert poisk([7, 7, 7], 7) == 0