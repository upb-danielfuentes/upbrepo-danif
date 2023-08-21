# Realice un algoritmo que permita capturar un numero del 1 al 12 y me indique a que mes corresponde, si se equivoca en el valor ingresado el programa finaliza
import sentry_sdk
def mes():
    try:
        mes = int(input("Ingrese un numero del 1 al 12: "))
        meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octumbre","Noviembre","Diciembre"]
        if mes < 1 or mes > 12:
            print("El numero ingresado no corresponde a un mes valido")
        else:
            print(f"El mes es {meses[mes-1]}")
    except ValueError as e:
        print("Error en el algoritmo",e)
        sentry_sdk.capture_exception(e)
        sentry_sdk.capture_message("Zero Division is Impossible")
mes()