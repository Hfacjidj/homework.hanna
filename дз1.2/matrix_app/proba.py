from matrix_app.matrix2x2 import Matrix2x2


m = Matrix2x2([[1, 2], [3, 4]])
assert m.determinant() == -2
m = Matrix2x2([[0, 0], [0, 0]])
assert m.determinant() == 0
