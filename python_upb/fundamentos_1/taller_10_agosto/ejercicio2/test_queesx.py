from ejercicio2 import queesx

def test_queesx_case_1():
    assert queesx(1, 2, 3, 0) == 0

def test_queesx_case_2():
    assert queesx(1, 2, 3, 1) == 1

def test_queesx_case_3():
    assert queesx(1, 2, 3, 2) == 2

def test_queesx_case_4():
    assert queesx(1, 2, 3, 3) == 3

def test_queesx_case_5():
    assert queesx(1, 2, 3, 4) == 3

def test_queesx_case_6():
    assert queesx(1, 2, 3, 5) == 3