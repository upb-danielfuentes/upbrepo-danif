# Realice un algoritmo que le permita a la tienda determinar el valor del descuento segun el monto de la compra

def ejercicio4():
    Monto = float(input("Ingrese el monto de la compra: "))
    if Monto >= 100000:
        Descuento = Monto * 0.10
    else:
        if Monto >= 200000:
            Descuento = Monto * 0.20
        else:
            print("No hay descuento")
    print("El descuento es: ", Descuento)
    print("Fin del programa")

ejercicio4()