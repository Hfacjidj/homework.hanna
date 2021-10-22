n = int(input('введите число'))
def digital(n):
    k1, k2 = 0, 1
    while n > 0:
        print(k1, end = ' ')
        k1, k2 = k2, k1 + k2 
        n = n - 1
digital(n)