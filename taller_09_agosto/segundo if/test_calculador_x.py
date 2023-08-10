# test_calculador_x.py
import calculador_x

def test_calcular_x_y_mayor_que_z():
    assert calculador_x.calcular_x(5, 3) == 1

def test_calcular_x_y_menor_o_igual_que_z():
    assert calculador_x.calcular_x(3, 5) == 2
