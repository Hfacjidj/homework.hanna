from sys import stdin
class matrix():
    def __init__(self, spisok): 
        self.mat = spisok
    def str(self):
        string = ''
        for i in self.mat:
            for j in i:
                string = string+'%s\t' %(j)
            string = string[:-1]
            string = string+'\n'
        string = string[:-1]
        return string
 
a = [[1,2,3],[4,5,6],[7,8,9]]
m = matrix(a)
print(m.str())
 
exec(stdin.read())
