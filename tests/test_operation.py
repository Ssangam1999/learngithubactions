from src.math_operation import add,subtract


def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0
    assert subtract(5,2) == 3


def test_sub():
    assert subtract(5,2) == 3
    assert subtract(5,4) == 1




