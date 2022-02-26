class Matrix:
    def __init__(self, strok=0, stolb=0):
        self.strok = strok
        self.stolb = stolb
        self.matrix = []

    def input(self):
        strok = int(input())
        stolb = int(input())
        for _ in range(strok):
            tn = []
            for _ in range(stolb):
                k = int(input("ведите число"))
                tn.append(k)
            self.matrix.append(tn)

    def __str__(self):
        return "\n".join(["\t".join(map(str, x)) for x in self.matrix])


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = Matrix(a)
m.input()
print(m)
