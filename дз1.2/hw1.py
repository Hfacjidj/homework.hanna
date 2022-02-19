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
        for i in self.matrix:
            for j in i:
                string = string+'%s\t' %(j)
            string = string[:-1]
            string = string+'\n'
        string = string[:-1]
        return string
 
a = [[1,2,3],[4,5,6],[7,8,9]]
m = Matrix(a)
m.input()
print(m)