def factorial(n):
    x = 1
    for i in range(2, n + 1):
        x *= i
    return x
n = int(input("Введите число "))
print(factorial(n))
assert factorial(0) == 1
assert factorial(5) == 120