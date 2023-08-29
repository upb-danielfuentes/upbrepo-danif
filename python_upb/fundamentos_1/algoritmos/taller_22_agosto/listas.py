# Manejo de listas en Python

def listas():
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    print(dias)
    dias.append("Lunes") # Agrega el elemento al final de la lista
    print(dias)
    dias.insert(0, "Lunes") # Inserta el elemento en la posición 0
    print(dias)
    dias.pop(0) # Elimina el elemento en la posición 0
    print(dias)
    dias.sort() # Ordena de forma ascendente
    print(dias)
    dias.reverse() # Ordena de forma descendente
    print(dias)
    dias.remove("Lunes") # Elimina el elemento "Lunes"
    print(dias)
    print(len(dias))
    print(dias.count("Lunes")) # Cuenta cuantas veces aparece "Lunes"
    print(dias.index("Lunes")) # Retorna la posición de "Lunes"
    print(dias[0]) # Retorna el elemento en la posición 0
    print(dias[0:3]) # Retorna los elementos desde la posición 0 hasta la 3
    print(dias[0:3:2]) # Retorna los elementos desde la posición 0 hasta la 3 de 2 en 2
    print(dias[::2]) # Retorna los elementos de 2 en 2
    print(dias[1::2]) # Retorna los elementos desde la posición 1 de 2 en 2
    print(dias[-1]) # Retorna el último elemento
    print(dias[-1:-4:-1]) # Retorna los elementos desde el último hasta el 4 de 1 en 1
    print(dias[-1::-1]) # Retorna los elementos desde el último hasta el primero de 1 en 1
    print(dias[-1:-4:-2]) # Retorna los elementos desde el último hasta el 4 de 2 en 2
    print(dias[-1::-2]) # Retorna los elementos desde el último hasta el primero de 2 en 2
    print(dias[0:3]) # Retorna los elementos desde la posición 0 hasta la 3
    print(dias[0:3:2]) # Retorna los elementos desde la posición 0 hasta la 3 de 2 en 2
    print(dias[::2]) # Retorna los elementos de 2 en 2

    #sumar dos listas
    lista1 = [1,2,3]
    lista2 = [4,5,6]
    lista3 = lista1 + lista2
    print(lista3)
    # Accesoa una lista dentro de otra lista
    listatotal= list((lista1,lista2))
    print(listatotal)

    #multiplicar una lista
    lista4 = lista1 * 3
    print(lista4)
    
listas()