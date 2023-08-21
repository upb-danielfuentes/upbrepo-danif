# Solicitar información al usuario
nombre = input("Ingrese su nombre: ")
salario_mensual = float(input("Ingrese su salario mensual: "))
n = int(input("Ingrese la cantidad de gastos a registrar: "))

# Inicializar listas para almacenar los detalles de los gastos
descripciones = []
montos = []

# Solicitar detalles de cada gasto
for i in range(n):
    descripcion = input(f"Ingrese la descripción del gasto {i + 1}: ")
    monto = float(input(f"Ingrese el monto del gasto {i + 1}: "))
    descripciones.append(descripcion)
    montos.append(monto)

# Calcular total de gastos y promedio
total_gastos = sum(montos)
promedio_gastos = total_gastos / n

# Calcular estado financiero
saldo = salario_mensual - total_gastos
estado_financiero = "sobrante" if saldo >= 0 else "faltante"

# Encontrar el gasto más caro y más barato
indice_gasto_caro = montos.index(max(montos))
gasto_caro = descripciones[indice_gasto_caro]

indice_gasto_barato = montos.index(min(montos))
gasto_barato = descripciones[indice_gasto_barato]

# Mostrar resumen
print("\nResumen de gastos:")
print(f"Total de gastos del mes: {total_gastos}")
print(f"Total de gastos versus total ganado: {saldo}")
print(f"Estado financiero: Tiene saldo {estado_financiero}")
print(f"Promedio de gastos por artículo: {promedio_gastos}")
print(f"Gasto más caro: {gasto_caro}")
print(f"Gasto más barato: {gasto_barato}")

# Opción para buscar gastos por encima o por debajo de un umbral
umbral = float(input("\nIngrese un umbral para buscar gastos (ingrese un valor negativo para buscar gastos por debajo del umbral): "))
print("\nGastos por encima del umbral:")

for descripcion, monto in zip(descripciones, montos):
    if monto > umbral:
        print(f"{descripcion}: ${monto}")
