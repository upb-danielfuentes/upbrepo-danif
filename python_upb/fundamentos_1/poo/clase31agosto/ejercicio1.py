# Clase del 31 de agosto de 2021
# Crear una función que reciba una lista de números y retorne una lista con los números pares de la lista recibida.
def DefPares(listanumeros):
    otra_lista = []
    for x in listanumeros:
        if x % 2 == 0:
            otra_lista.append(x)
    return otra_lista

ListaEnvio = [1,2,3,4,5,6,7,8,9]
listamia = DefPares(ListaEnvio)
print (listamia)


def LambaPares(listanumeros):
    return list(filter(lambda x: x%2 == 0, listanumeros))

ListaEnvio = [1,2,3,4,5,6,7,8,9,10,11,111,11111,232,234,345,4564,675,674,345,534,53,564,75,78674,5643,45]
listamia = LambaPares(ListaEnvio)
print (listamia)

suma= lambda x,y: x+y
print (suma(2,3))


