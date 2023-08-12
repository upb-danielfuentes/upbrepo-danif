# test_descuentos.py
import descuentos

def test_descuento_mayor_o_igual_a_100000():
    assert descuentos.ejercicio4(150000) == 15000.0

def test_descuento_mayor_o_igual_a_200000():
    assert descuentos.ejercicio4(250000) == 25000.0

def test_descuento_menor_a_100000():
    assert descuentos.ejercicio4(50000) == 0.0
