#   While > Cuando no sepamos la cantidad de algo
#   For > Cuando sabemos la cantidad de algo
#   Estructura repetitiva que permite realizar acciono acciones varias veces
#   Solo si se cumple una o varias condiciones

#   Realice un algoritmo que permita capturar 40 valores siempre y cuando el siguiente sea 
#   mayor que el anterior, al final debe mostrar los numeros en una lista, 
#   Su cantidad de posiciones y la sumatoria de los numero


def capturar():

    ListaNumero=[]
    cant = 0
    totalSum = 0
    num = 0
    ultimo =0

    while cant < 40:
        ultimo = num
        num=int(input("ingrese numero: "))
        if num >= ultimo:
            ListaNumero.append(num)
        else:
            break
        cant+=1
    for x in ListaNumero:
        totalSum +=x

    print(ListaNumero)
    print("🔊 La cantidad de posiciones es: ",len(ListaNumero))
    print("🗯️ La sumatoria de los numeros es: ",totalSum)

capturar()


