from ejercicio3 import mayordelostres

def test_mayordelostres_distinct_values():
    assert mayordelostres(5, 10, 3) == 10
    assert mayordelostres(8, 2, 6) == 8
    assert mayordelostres(1, 1, 1) == "Los tres valores son iguales"

def test_mayordelostres_negative_values():
    assert mayordelostres(-5, -10, -3) == -3
    assert mayordelostres(-8, -2, -6) == -2
    assert mayordelostres(-1, -1, -1) == "Los tres valores son iguales"

def test_mayordelostres_mixed_values():
    assert mayordelostres(5, -10, 3) == 5
    assert mayordelostres(-8, 2, -6) == 2
    assert mayordelostres(-1, 1, -1) == 1
    assert mayordelostres(0, 0, 0) == "Los tres valores son iguales"
