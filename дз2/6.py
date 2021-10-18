a = []
t = input()
y = int(input())
for i in t:
    if i.isdigit():
        a.append(i)
print(a[y - 1])