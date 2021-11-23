def factorial(n):
    x = 1
    for i in range(2, n + 1):
        x *= i
    return x
n = int(input("Введите число "))
print(factorial(n))

def function():
    assert function(3) == 6
    assert function(0) == 1