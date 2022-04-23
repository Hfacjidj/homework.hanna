from matrix_app.matrix import Matrix


def test_init():
    f = Matrix()
    assert f.stolb == 1
    assert f.strok == 1
    assert f.matrix == [[0]]


def test_str():
    f = Matrix([[2, 1], [3, 4]])
    j = str(f)
    assert j == "2\t1\n3\t4"


def test_input(mocker):
    mocker.patch("builtins.input", side_effect=["1", "2", "10", "11"])
    a = Matrix()
    a.input()
    assert a.stolb == 2
    assert a.strok == 1
    assert a.matrix == [[10, 11]]
