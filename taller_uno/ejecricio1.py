# Realice un algoritmo que le sirva a una casa de cambio de moneda a realizar los cálculos
# para que cuando un cliente llegue, El ingrese el valor en pesos que desea cambiar y el
# software le indique ese valor en pesos convertido a dólares, soles y rumpias.
# Es importante que revise las tasas de conversión de Colombia para esos valores y realice los cálculos adecuados
# recuerde que cuando les muestre el resultado a los clientes debe indicar
# el valor que ingreso, el nombre del cliente, el valor del dólar y valor de conversión en dólares,
# el valor del sol y valor de conversión en soles y el valor de la rumpia y el valor de conversión en rumpias


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
