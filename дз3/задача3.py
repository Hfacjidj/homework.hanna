def digital(n):
    k1, k2 = 0, 1
    for n in range(n):
        print(k1, end = ' ')
        k1, k2 = k2, k1 + k2
n = int(input('введите число'))     
digital(n)