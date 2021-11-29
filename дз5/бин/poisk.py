d = [1, 9, 2, 8, 3, 7, 4, 6, 5]
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
assert poisk([1, 9, 2, 8, 3, 7, 4, 6, 5], 1) == 0
assert poisk([1, 9, 2, 8, 3, 7, 4, 6, 5], 0) == None
assert poisk([], 1) == None
assert poisk([1, 9, 2, 8, 3, 7, 1, 4, 6, 5], 1) == 0