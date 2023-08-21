# Definir los tipos de empanadas y sus precios
menu_empanadas = {
    "Carne": 2.5,
    "Pollo": 2.0,
    "Queso": 1.8,
    "Papa": 2.2
}

# Solicitar información al usuario sobre las empanadas a comprar
num_empanadas = int(input("Ingrese el número de empanadas a comprar: "))
total_costo = 0

for i in range(num_empanadas):
    print(f"\nEmpanada {i + 1}:")
    print("Tipos de empanadas disponibles:")
    for tipo in menu_empanadas:
        print(f"- {tipo}")
    
    tipo_empanada = input("Ingrese el tipo de empanada: ")
    if tipo_empanada in menu_empanadas:
        cantidad = int(input("Ingrese la cantidad: "))
        costo_empanada = menu_empanadas[tipo_empanada]
        costo_total_empanada = cantidad * costo_empanada
        total_costo += costo_total_empanada
        print(f"Costo de {cantidad} empanadas de {tipo_empanada}: ${costo_total_empanada:.2f}")
    else:
        print("Tipo de empanada no válido.")

# Mostrar el costo total de la compra
print(f"\nCosto total de la compra: ${total_costo:.2f}")
