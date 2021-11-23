def ted(b):
    sr = sum(b) / len(b)
    print('Среднее арифметическое =', sr)
n = input('ввод ')
b = list()
while n != '':
    b.append(float(n))
    n = input('введи ')
ted(b) 