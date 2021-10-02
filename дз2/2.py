s = input()
s = s.replace(' ','')
k = list(s)
n = list()
for i in range (0, len(k)):
    n.append(int(k[i]))
n.sort()
n.reverse()
v = str()
for i in range(0, len(n)):
    v = v+str(n[i])
print (v)
