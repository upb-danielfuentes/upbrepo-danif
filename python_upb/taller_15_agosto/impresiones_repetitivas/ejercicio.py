# Realizar un sistema de calificaciones de alumnos, el sistema debe captura las calificaciones
# de un grupo de estudiantes donde no sabemos la cantidad pero si sabemos que son 3 notas en total
# El algoritmo debe imprimir el nombre del estudiante junto con su nota definitiva
# importante saber que la nota final se calcula con el promedio de las 3 notas

def calcularNota():
    print ("Bienvenido al sistema de calificaciones")
    print ("Por favor ingrese los siguientes datos")
    cantidadEstu = int(input("Ingrese la cantidad de estudiantes del curso: "))
    for i in range(1,(cantidadEstu+1)):
        nombre = input("Ingrese el nombre del estudiante: ")
        nota1 = float(input(f"Ingrese la primera nota del estudiante {nombre}: "))
        nota2 = float(input(f"Ingrese la segunda nota del estudiante {nombre}: "))
        nota3 = float(input(f"Ingrese la tercera nota del estudiante {nombre}: "))
        notaFinal = (nota1 + nota2 + nota3) / 3
        if notaFinal >= 3.0:
            print("El estudiante: ", nombre, "esta aprobado" , "con una nota de: ", notaFinal)
        else:
            print("El estudiante: ", nombre, "esta reprobado", "con una nota de: ", notaFinal)
calcularNota()