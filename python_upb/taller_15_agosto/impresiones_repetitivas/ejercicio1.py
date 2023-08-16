# Realice un algoritmo que permita capturar el nombre de la persona
# y lo imprima la cantidad de veces que quiera

def imprimirNombre():
    nombre = input("Ingrese su nombre: ")
    cantidad = int(input("Ingrese la cantidad de veces que quiere imprimir su nombre: "))
    for i in range(cantidad):
        print(nombre)
imprimirNombre()
