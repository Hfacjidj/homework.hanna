def function():
    f = input("Введите элементы списка\n")
    b = list()
    while f != '':
        b.append(f)
        f = input()
    if len(b) == len(set(b)):
        print("True")
    else:
        print("False")
print(function())

def function():
    assert function([1, 2, 3, 4, 5]) == "True"
    assert function([1, 2, 2, 3]) == "False"