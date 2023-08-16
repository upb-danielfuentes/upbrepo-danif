# Realice un algoritmo que permita capturar el nombre de la persona
# y lo imprima la cantidad de veces que quiera

import sentry_sdk

sentry_sdk.init(
    dsn="https://3f05934c49e0a8f851715c05a7c34b31@o4505677157695488.ingest.sentry.io/4505681394073600",
    traces_sample_rate=1.0
)

def imprimirNombre():
    try:
        nombre = input("Ingrese su nombre: ")
        cantidad = int(input("Ingrese la cantidad de veces que quiere imprimir su nombre: "))
        for i in range(cantidad):
            print(nombre)
    except ValueError as e:
        sentry_sdk.capture_exception(e)
        sentry_sdk.capture_message("El valor ingresado no es un número")
imprimirNombre()
