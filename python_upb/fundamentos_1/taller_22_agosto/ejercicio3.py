# Realice un algoritmo que le solicte al usuario un numero tras otro, hasta que ingrese un numero negativo , 
# luego debe mostrar la suma de los numeros, 
# el listado de los numero
# el numero mayor y menor de los numeros ingresados


import sentry_config

class Ejemplos:
    def __init__(self):
        try:
            numeros = []
            while True:
                numero = int(input("Ingrese un numero: "))
                if numero < 0:
                    break
                numeros.append(numero)
            print("La suma de los numeros es: ", sum(numeros))
            print("El listado de los numeros es: ", numeros)
            print("El numero mayor es: ", max(numeros))
            print("El numero menor es: ", min(numeros))
        except Exception as e:
            sentry_config.capture_exception(e)
            sentry_config.capture_message("Error en el script principal")

if __name__ == "__main__":
    main = Ejemplos()

