# Determine la suma del valor menor y mayor de un grupo de cuatro datos dados

def suma_menor_mayor():
    # Obtener los datos del usuario
    dato1 = float(input("Ingrese el dato 1: "))
    dato2 = float(input("Ingrese el dato 2: "))
    dato3 = float(input("Ingrese el dato 3: "))
    dato4 = float(input("Ingrese el dato 4: "))

    # Encontrar el valor menor
    if dato1 <= dato2 and dato1 <= dato3 and dato1 <= dato4:
        valor_menor = dato1
    elif dato2 <= dato1 and dato2 <= dato3 and dato2 <= dato4:
        valor_menor = dato2
    elif dato3 <= dato1 and dato3 <= dato2 and dato3 <= dato4:
        valor_menor = dato3
    else:
        valor_menor = dato4

    # Encontrar el valor mayor
    if dato1 >= dato2 and dato1 >= dato3 and dato1 >= dato4:
        valor_mayor = dato1
    elif dato2 >= dato1 and dato2 >= dato3 and dato2 >= dato4:
        valor_mayor = dato2
    elif dato3 >= dato1 and dato3 >= dato2 and dato3 >= dato4:
        valor_mayor = dato3
    else:
        valor_mayor = dato4

    # Calcular la suma del valor menor y mayor
    suma_valores = valor_menor + valor_mayor

    # Mostrar el resultado
    print(f"La suma del valor menor y mayor es: {suma_valores}")

suma_menor_mayor()