def f():
    l = list(input('Введите список'))
    for x in set(l):
        y = l.count(x)
        print(x, ':', y)		   
print(f()) 