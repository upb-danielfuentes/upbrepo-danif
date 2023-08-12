# una empresa con 3 departamentos tiene establecido un plan de incentivos para sus vendedores. 
# Al final del periodo, a cada departamento se le pide que importe el global de las ventas. 
# A los departamentos que excedan el 33% de las ventas totales se les adiciona al salario de los vendedore un porcentaje equivalente al 20% del salario mensual. las nominas de los 3 departamentos son iguales. 
# Si se tiene los siguientes datos:
# ventas del depa 1
# ventas del depa 2
# ventas del depa 3
# salario de los vendedores de cada departamento 
# Hacer un algoritmo que determine cuanto reciben los vendedores de cada departamento al finalizar el periodo

def calcular_incentivo(ventas, total_ventas, salario):
    incentivo = 0.2 * salario if ventas > 0.33 * total_ventas else 0
    return salario + incentivo

# Ingresar los datos de ventas y salarios
ventas_depa1 = float(input("Ventas del departamento 1: "))
ventas_depa2 = float(input("Ventas del departamento 2: "))
ventas_depa3 = float(input("Ventas del departamento 3: "))
salario_vendedores = float(input("Salario de los vendedores: "))

ventas_totales = ventas_depa1 + ventas_depa2 + ventas_depa3

# Calcular los incentivos y mostrar los resultados
salario_depa1 = calcular_incentivo(ventas_depa1, ventas_totales, salario_vendedores)
salario_depa2 = calcular_incentivo(ventas_depa2, ventas_totales, salario_vendedores)
salario_depa3 = calcular_incentivo(ventas_depa3, ventas_totales, salario_vendedores)

print("Salarios después de los incentivos:")
print(f"Departamento 1: ${salario_depa1:.2f}")
print(f"Departamento 2: ${salario_depa2:.2f}")
print(f"Departamento 3: ${salario_depa3:.2f}")
