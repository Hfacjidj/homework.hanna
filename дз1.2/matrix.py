from abc import ABC, abstractmethod


class Matrix(ABC):
    def __init__(self, matrix=[[0]]):
        self.strok = 1
        self.stolb = 1
        self.matrix = matrix

    def input(self):
        self.matrix = []
        self.strok = int(input("Введите кол-во строк: "))
        self.stolb = int(input("Введите кол-во столбцов: "))
        for _ in range(self.strok):
            tn = []
            for _ in range(self.stolb):
                k = int(input("Введите число: "))
                tn.append(k)
            self.matrix.append(tn)

    def __str__(self):
        return "\n".join(["\t".join(map(str, x)) for x in self.matrix])

@abstractmethod
def determinant(self):
        raise NotImplementedError