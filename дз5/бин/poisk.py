d = [1, 2, 3, 4, 5, 6, 7]
d = sorted(d)
def poisk(d, n):
    lower = 0
    upper = len(d) - 1
    while lower <= upper:
        center = (lower + upper) // 2
        if d[center] == n:
            return center
        elif d[center] > n:
            upper = center - 1
        elif d[center] < n:
            lower = center + 1
    return None


n = int(input("Элемент, который необходимо обнаружить: "))
print(poisk(d, n))
assert poisk([1, 2, 3, 4, 5, 6, 7], 5) == 4
assert poisk([7, 22, 34, 41, 75, 69, 77], 7) == 0
assert poisk([5, 2345, 33245, 42, 55, 634, 77], 1) == None
assert poisk([], 1) == None
assert poisk([7, 7, 7], 7) == 1