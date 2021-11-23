from задача1 import itog

sum = int()
a = itog()
for i in range(1,len(a) + 1):
    print(i)
    sum += i
v = round(sum/len(a))
print(v)