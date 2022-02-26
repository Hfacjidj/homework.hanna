class Matrix:
    def __init__(self, strok=1, stolb=1):
        self.strok = strok
        self.stolb = stolb
        self.matrix = [[0]]

    def input(self):
        self.strok = int(input())
        self.stolb = int(input())
        for _ in range(self.strok):
            tn = []
            for _ in range(self.stolb):
                k = int(input("ведите число"))
                tn.append(k)
            self.matrix.append(tn)

    def __str__(self):
        return "\n".join(["\t".join(map(str, x)) for x in self.matrix])


m1 = Matrix()
print(m1)

m = Matrix()
m.input()
print(m)
