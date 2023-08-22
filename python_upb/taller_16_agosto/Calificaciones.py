# Realice un algoritmo que permita ingresar cinco calificaciones por estudiante, 
# de las materias de programacion 1, programacion 2, desarrollo de software, bases de datos, Estructura de datos. 
# La cantidad de estudiantes los ingresa el profesor. 
# Al final debe mostrar el nombre del estudiante, la calificacion de cada una de las materias y 
# realizar el calculo promedio por notas de cada asigntura.

print ('Bienvenido al sistema de calificaciones')
studentsAmount = int(input('Ingrese la cantidad de estudiantes: '))
subject = ['Programacion 1', 'Programacion 2', 'Desarrollo de software', 'Bases de datos', 'Estructura de datos']
programacion1 = []
programacion2 = []
desarrolloSoftware = []
basesDeDatos = []
estructuraDeDatos = []
studentsName = []
subjectAverage = []

# Procedimiento
# Recoleccion de datos
for i in range(0, studentsAmount):
  studentsName.append(input(f'Ingrese el nombre del estudiante {i + 1}: '))
  programacion1.append(float(input(f'Ingrese la calificacion de {subject[0]}: ')))
  programacion2.append(float(input(f'Ingrese la calificacion de {subject[1]}: ')))
  desarrolloSoftware.append(float(input(f'Ingrese la calificacion de {subject[2]}: ')))
  basesDeDatos.append(float(input(f'Ingrese la calificacion de {subject[3]}: ')))
  estructuraDeDatos.append(float(input(f'Ingrese la calificacion de {subject[4]}: ')))


