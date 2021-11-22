def function():
    n = int(input("Введите n :\n"))
    if n == 0:
        return 1
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
            return factorial
print(function())