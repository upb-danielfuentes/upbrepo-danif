# Parametros
# son los valores que se le pasan a la función para que esta los procese
# Ejemplo:
def ejemplo_funcion(nombre, apellido, grado):
    print("Hola, mi nombre es " + nombre + " " + apellido + " y estoy en " + grado + " grado")
ejemplo_funcion("Juan", "Perez", "11")
ejemplo_funcion(input("Ingrese su nombre: "), input("Ingrese su apellido: "), input("Ingrese su grado: "))
# Argumentos
# son los valores que se le pasan a la función para que esta los procese
# Ejemplo:
def ejemplo_funcion(nombre, apellido, grado):
    print("Hola, mi nombre es " + nombre + " " + apellido + " y estoy en " + grado + " grado")
ejemplo_funcion("Juan", "Perez", "11")
ejemplo_funcion(input("Ingrese su nombre: "), input("Ingrese su apellido: "), input("Ingrese su grado: "))
# Return
# es la palabra reservada que se utiliza para retornar un valor de una función
# Ejemplo:
def ejemplo_funcion(nombre, apellido, grado):
    return "Hola, mi nombre es " + nombre + " " + apellido + " y estoy en " + grado + " grado"
print(ejemplo_funcion("Juan", "Perez", "11"))
print(ejemplo_funcion(input("Ingrese su nombre: "), input("Ingrese su apellido: "), input("Ingrese su grado: ")))
# Ejemplo de función con return
def suma(a, b):
    return a + b
print(suma(5, 6))
# Ejemplo de función con return
def resta(a, b):
    return a - b
print(resta(5, 6))
# Ejemplo de función con return
def multiplicacion(a, b):
    return a * b
print(multiplicacion(5, 6))
# Ejemplo de función con return
def division(a, b):
    return a / b
print(division(5, 6))
# Ejemplo de función con return
def potencia(a, b):
    return a ** b
print(potencia(5, 6))
# Ejemplo de función con return
def modulo(a, b):
    return a % b
print(modulo(5, 6))
# Ejemplo de función con return
def division_entera(a, b):
    return a // b
print(division_entera(5, 6))
