from msilib import type_localizable


class Matrix():
    def __init__(self, strok = 0, stolb = 0, elements = 0): 
        self.strok = strok
        self.stolb = stolb
        self.elements = elements
        self.matrix = []
    def input(self):
        strok = int(input())
        stolb = int(input())
        for i in range(strok):
            tn = []
            for j in range(stolb):
                k = int(input('ведите число'))
                tn.append(k)
            self.matrix.append(tn)
    def __str__(self):
        string = ''
        for i in self.matrix: #перебирает вложенные в нее списки
            for j in i:
                string = string+'%s\t' %(j) #берет элемент j добавляет пробел после него, превращает в стринговую переменную и закидывает в отдельную переменную стринг\t- добавляет пробел
            string = string [:-1] #перебирает любую итерируемую вещь, в обратном направлении
            string = string+'\n' #добавляет переход на новую строку
        string = string[:-1]
        return string
 
a = [[1,2,3],[4,5,6],[7,8,9]]
m = Matrix(a)
m.input()
print(m)