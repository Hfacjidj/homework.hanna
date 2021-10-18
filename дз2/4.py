a = input()
x = a.count('(') 
y = a.count(')')
if x > y:
    print('не хватает закрывающихся скобок', x-y)
elif y > x:
    print('не хватает открывающихся скобок',y-x)
else:
    print('все хорошо')