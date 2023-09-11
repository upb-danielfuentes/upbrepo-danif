# Realice un algoritmo que permita capturar las ventas de vehiculos
# de tres tiendas diferentes, teniendo en cuenta que los vendedores
# ingresan las ventas por semana, y se debe calcular el total de ventas
# por la marca de autos y las ventas totales de cada tienda.

# Tienda 1: Toyota, Mazda, Chevrolet
# Tienda 2: Renault, Kia, Hyundai
# Tienda 3: Ferrari, Lamborghini, Porsche

def tiendas():

    totalConcesionario = 0
    for i in range(1,4):
        print("---------------------------------------------------------------")
        print(f"Ingrese las ventas de la Tienda {i}")
        print("---------------------------------------------------------------")
        ventasSemana = 0
        for j in range(1,5):
            print("---------------------------------------------------------------")
            print(f"Semana {j}")
            print("---------------------------------------------------------------")
            ventasSemana = ventasSemana + float(input("Ingrese las ventas: "))
        print("---------------------------------------------------------------")
        print(f"Total de ventas en la tienda {i} es de: {ventasSemana} USD")
        print("---------------------------------------------------------------")
        totalConcesionario = totalConcesionario + ventasSemana
    print("---------------------------------------------------------------")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f"Total de ventas del concesionario fue de: {totalConcesionario} USD")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("---------------------------------------------------------------")
    if totalConcesionario < 100000:
        print("---------------------------------------------------------------")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("El concesionario no fue rentable mi fai")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("---------------------------------------------------------------")

tiendas()


