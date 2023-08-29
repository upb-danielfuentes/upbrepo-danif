import pytest
from ejercicio5 import suma_menor_mayor  # Importa tu función desde el módulo

# Pruebas unitarias utilizando pytest
def test_suma():
    assert suma_menor_mayor(1, 2, 3, 4) == 5
    assert suma_menor_mayor(-1, -2, -3, -4) == -5
    assert suma_menor_mayor(10, 5, 8, 3) == 13
    assert suma_menor_mayor(0, 0, 0, 0) == 0

if __name__ == "__main__":
    pytest.main()
