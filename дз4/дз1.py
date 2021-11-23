def d():
    x = input('Введите что-нибудь') 
    b = []
    while x != '':  
        b.append(x)
        x = input()
    l = int(input('Введите число k = '))
    while l > 0:
        b = b[-1:] + b[:-1]
        l = l - 1
    return b 
print(d())

def d():
    assert function([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
    assert function([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert function([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]
    assert function([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert function([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]
