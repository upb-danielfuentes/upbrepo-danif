# Casa de Cambio: Dolares, Soles y Ripuas

def casa_de_cambio():
    # Tasas de conversión
    tasa_dolar_cop = 4030
    tasa_dolar_soles = 1093.15
    tasa_dolar_rupias = 48.7

    # Pedir datos al cliente
    nombre_cliente = input("Ingrese su nombre: ")
    valor_pesos = float(input("Ingrese el valor en pesos que desea cambiar: "))

    # Realizar los cálculos
    valor_dolares = valor_pesos / tasa_dolar_cop
    valor_soles = valor_pesos / tasa_dolar_soles
    valor_rupias = valor_pesos / tasa_dolar_rupias

    # Mostrar resultados
    print("\nHola,", nombre_cliente , "el valor que ingresaste en pesos (COP) fue de: ",valor_pesos)
    print("El valor del dolar (USD) hoy esta en:",tasa_dolar_cop, "La conversion en dólares (USD) seria de: ", valor_dolares)
    print("El valor del sol (PEN) hoy esta en:" ,tasa_dolar_soles , "La conversion en soles (PEN) seria de: ", valor_soles)
    print("El valor de las rupias (INR) hoy esta en:", tasa_dolar_rupias , "La conversion en rupias (PEN) seria de: ", valor_rupias)

# Ejecutar el programa
casa_de_cambio()
