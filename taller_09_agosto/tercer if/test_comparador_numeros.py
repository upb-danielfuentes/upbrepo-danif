# test_comparador_numeros.py
import comparador_numeros

def test_comparar_numeros_primer_mayor():
    assert comparador_numeros.comparar_numeros(5, 3) == "El primer numero es mayor que el segundo"

def test_comparar_numeros_iguales():
    assert comparador_numeros.comparar_numeros(3, 3) == "El segundo numero es igual que el primero"

def test_comparar_numeros_segundo_mayor():
    assert comparador_numeros.comparar_numeros(3, 5) == "El numero B es mayor"
