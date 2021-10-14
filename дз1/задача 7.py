a = 0
x = int(input(' ввести х'))
y = int(input(' ввести y'))
for i in range(x, y+1):
    if i % 5 == 0:
        a += i
    print(a)
