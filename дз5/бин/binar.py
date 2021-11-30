from lister import funk


print('Введите список >> ')
a = funk()
a.sort(key=int)
print(a)
k = int(input('Введите искомый элемент >> '))


def binar(a, k):
    if a == []:
        return 'Введённый спиcок пуст'
    else:
        s = len(a) // 2
        e = len(a) - 1
        b = 0
        while int(a[s]) != k and b <= e:
            if k > int(a[s]):
                b = s + 1
            else:
                e = s - 1
            s = (b + e) // 2
        if b > e:
            return None
        else:
            for i in range(s+1):
                if a[i] == a[s] and i < s:
                    s = i
            return s


print(binar(a, k))
assert binar([1, 2, 3, 4, 5, 6, 7], 5) == 4
assert binar([7, 22, 34, 41, 69, 75, 77], 7) == 0
assert binar([5, 42, 55, 77, 534, 645, 777], 1) is None
assert binar([], 1) == 'Введённый спиcок пуст'
assert binar([7, 7, 7], 7) == 0 