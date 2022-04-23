from matrix_app.matrix2x2 import Matrix2x2


def test_determinat():
    a = Matrix2x2([[2, 3], [1, 4]])
    k = a.determinant()
    assert k == 5
