n = int(input())
def vrema(n):
    if n in [12, 1, 2]:
        print ('winter')
    elif n in [3, 4, 5]:
        print ('spring')
    elif n in [6, 7, 8]:
        print ('summer')
    elif n in [9, 10, 11]:
        print ('autumn')
    else:
        print('нету такого месяца')
print(vrema(n))