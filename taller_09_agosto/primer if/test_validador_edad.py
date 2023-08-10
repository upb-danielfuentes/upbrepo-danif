# test_validador_edad.py
import validador_edad

def test_es_mayor_de_edad():
    assert validador_edad.es_mayor_de_edad(20) == True
    assert validador_edad.es_mayor_de_edad(18) == True
    assert validador_edad.es_mayor_de_edad(17) == False
    assert validador_edad.es_mayor_de_edad(0) == False
