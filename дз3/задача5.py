def ted(b):
    sr = sum(b) / len(b)
    print('Среднее арифметическое =', sr)
b = list()
n = (input('Введи  '))
while n != '':
    b.append(float(n))
    n = (input('введи '))
ted(b) 