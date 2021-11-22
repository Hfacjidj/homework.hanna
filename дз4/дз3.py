def function(f):
    try:
        assert len(f) == len(set(f))
        return True
    except AssertionError:
        return False

a = list()
print("Введите список : ")
i = input()
a.append(i)
while i != "":
    i = input()
    a.append(i)
a.pop()

print(function(a))