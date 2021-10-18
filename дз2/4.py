a = input()
x = a.count('(') 
y = a.count(')')
if x > y:
    print('не хватает закрывающихся скобок')
elif y > x:
    print('не хватает открывающихся скобок')
else:
    print('все хорошо')