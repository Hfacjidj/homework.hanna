def itog():
    x = input("Введите что-нибудь")
    b = list()
    while x != '': #пока не будет введена пустая строка будет выполнятся...
        b.append(x) #append -добавляет в список b элементы х
        x = input()
        print(b)
itog()