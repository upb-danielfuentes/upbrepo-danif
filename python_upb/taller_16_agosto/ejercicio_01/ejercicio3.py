# realice un algoritmo que permita caputara un numero inferior a 50
# que sea entero positivo, y muestre por consola la impresion de los valores ascendente desde 1 hasta el numero, y que sean inpares
import sentry_sdk
def numero(): 
    try:
        num = int(input("Ingrese un numero entero positivo menor a 50: "))
        if num < 0 or num > 50:
            print("El numero ingresado no es valido")
        else:
            for i in range(1,num+1,2):
                print(i)
    except ValueError as e:
        sentry_sdk.capture_exception(e)
        sentry_sdk.capture_message("Impossible")
numero()