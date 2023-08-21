# Date: 16/08/2021
# Realizar un algoritmo que permita registrar la produccion (unidades)
# logradas por operario a lo largo de la semana (lunes a sabado)
# Debe mostrar si el empleado recibira incentivos sabiendo que el
# promedio de produccion minima es de 100 unidades
import sentry_sdk
def produccion():
    print("Bienvenido al sistema de incentivos")
    try:
        nombre = input("Ingrese su nombre: ")
        produccion = 0
        diassem = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
        for i in range(0,6):
            produccion = produccion + int(input(f"Ingrese la producción del día {diassem[i]}: "))
        total = produccion / 6
        if total < 100:
            print(f"El empleado {nombre} ,No recibirá incentivos, ya que la produccion fue de {total}")
        else:
            print(f"El empleado {nombre}, Recibirá incentivos, ya que la produccion fue de {total}")
    except ValueError as e:
        print ("Error en el algoritmo",e)
        sentry_sdk.capture_exception(e)
        sentry_sdk.capture_message("Error en el algoritmo")

produccion()