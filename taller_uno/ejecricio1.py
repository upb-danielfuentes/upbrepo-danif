# Casa de Cambio: Dolares, Soles y Ripuas

def casa_de_cambio():
    # Tasas de conversión
    tasa_dolar_cop = 3000
    tasa_dolar_soles = 4.5
    tasa_dolar_rupias = 80

    # Pedir datos al cliente
    nombre_cliente = input("Ingrese su nombre: ")
    valor_pesos = float(input("Ingrese el valor en pesos que desea cambiar: "))

    # Realizar los cálculos
    valor_dolares = valor_pesos / tasa_dolar_cop
    valor_soles = valor_pesos / tasa_dolar_soles
    valor_rupias = valor_pesos / tasa_dolar_rupias

    # Mostrar resultados
    print("\nResultado para:", nombre_cliente)
    print("Valor ingresado en pesos: COP", valor_pesos)
    print("Valor en dólares (USD): USD", valor_dolares)
    print("Valor en soles (PEN): PEN", valor_soles)
    print("Valor en rupias (INR): INR", valor_rupias)

# Ejecutar el programa
casa_de_cambio()
