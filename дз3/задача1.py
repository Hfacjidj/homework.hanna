def itog():
    x = input('Введите что-нибудь')
    b = []
    while x != '':  
        b.append(x)
        x = input()
        print(b)
print(itog())