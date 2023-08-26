# Lista de propiedades de las listas en python

DiasSemanas = ["lunes", "Martes", "Martes", "Martes", "Martes", "Miercoles"]

# Copiar los datos de una lista a otra
Dias = DiasSemanas.copy()

print(Dias)

# Insertar valores a una lista desde una posición especifica
DiasSemanas.insert(0, "Jueves")
print(DiasSemanas)

# Para insertar en la cola o al final de la lista
DiasSemanas.append("Sabado")

# Esto me permite modificaciones de los valores guardados en la posición X
DiasSemanas[1] ="Lunes"

print(DiasSemanas)

#Eliminar solo el ultimo de la lista 
DiasSemanas.pop()
print(DiasSemanas)

# Eliminar una posición en especifico
DiasSemanas.pop(0)
print(DiasSemanas)

# Elimina los datos que esten segun el valor ingresado
DiasSemanas.remove("Martes")
print(DiasSemanas)

# Metodo para ordenar de forma ascendente una lista es
DiasSemanas.sort()

# Metodo para ordenar de forma descendente una lista es 
DiasSemanas.sort(reverse=True)

# Ordena de mayor a menor
DiasSemanas.reverse()

# Count permite contar cuantos valores repetidor existen de un dato
print(DiasSemanas.count("Martes"))

# Len que permite indicar el total de posiciones reales de una lista
print(len(DiasSemanas))

# Suma de listas
Finde = ["Sabado", "Domingo"]

#ListTotal = DiasSemanas + Finde

# Acceso a una lista dentro de otra lista
ListTotal = list((DiasSemanas, Finde))
print(ListTotal)
print('Acceso a una lista dentro de otra lista')
print(ListTotal[0][4])
print ("----------------------")

myName = list("123456789")
print(myName)

# Para borrar datos de forma total
DiasSemanas.clear()
print(DiasSemanas)

