def spisok():
    b = []
    while x != '':
        b.append(x) 
        x = input()
    if '' in b:
        b.remove('')
    for x in set(b):
        l = b.count(x)
    print(x, '-', b.count(x), 'повторений')
spisok()