import pytest
from rangoedad import obtener_rango_edad, obtener_genero

def test_obtener_rango_edad():
    assert obtener_rango_edad(2000) == "joven"
    assert obtener_rango_edad(1975) == "adulto"
    assert obtener_rango_edad(2005) == "joven"
    assert obtener_rango_edad(2023) == "bebe"
    assert obtener_rango_edad(1900) == "adulto mayor"
    assert obtener_rango_edad(3000) is None
    assert obtener_rango_edad(-100) is None

def test_obtener_genero():
    assert obtener_genero("f") == "Mujer"
    assert obtener_genero("m") == "Hombre"
    assert obtener_genero("F") == "Mujer"
    assert obtener_genero("M") == "Hombre"
    assert obtener_genero("Otro") is None

if __name__ == "__main__":
    pytest.main()
