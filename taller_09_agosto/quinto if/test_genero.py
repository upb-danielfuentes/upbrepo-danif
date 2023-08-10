# test_genero.py
import genero

def test_genero_femenino():
    assert genero.ejercicio5("M") == "Sumerce es Mujer"

def test_genero_masculino():
    assert genero.ejercicio5("H") == "Sumerce es Hombre"

def test_genero_no_binario():
    assert genero.ejercicio5("X") == "Genero no Binario"
