def calcular_incentivo(ventas, total_ventas, salario):
    incentivo = 0.2 * salario if ventas > 0.33 * total_ventas else 0
    return salario + incentivo

# Función para calcular los salarios y realizar pruebas unitarias
def calcular_salarios(ventas_depa1, ventas_depa2, ventas_depa3, salario_vendedores):
    ventas_totales = ventas_depa1 + ventas_depa2 + ventas_depa3

    salario_depa1 = calcular_incentivo(ventas_depa1, ventas_totales, salario_vendedores)
    salario_depa2 = calcular_incentivo(ventas_depa2, ventas_totales, salario_vendedores)
    salario_depa3 = calcular_incentivo(ventas_depa3, ventas_totales, salario_vendedores)
    
    return salario_depa1, salario_depa2, salario_depa3

# Pruebas unitarias usando pytest
def test_calcular_salarios():
    assert calcular_salarios(1000, 2000, 3000, 1000) == (1400.0, 1400.0, 1800.0)
    assert calcular_salarios(500, 750, 1000, 1500) == (1500.0, 1500.0, 1700.0)
    assert calcular_salarios(2000, 3000, 4000, 2000) == (2400.0, 2400.0, 2800.0)

# Ejecutar las pruebas si este archivo es ejecutado directamente
if __name__ == "__main__":
    import pytest
    pytest.main()
