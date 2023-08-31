# Funciones
# Las funciones son un conjunto de instrucciones que se ejecutan cuando son llamadas
listaEstudiantes = []
def ejemplo_funcion():
    print("Hola, soy una función")
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    grado = input("Ingresa tu grado: ")
    print("Hola, mi nombre es " + nombre + " " + apellido + " y estoy en " + grado + " grado")
    listaEstudiantes.append(nombre + " " + apellido + " " + grado)
    
# Llamada a la función
ejemplo_funcion()
print(listaEstudiantes)