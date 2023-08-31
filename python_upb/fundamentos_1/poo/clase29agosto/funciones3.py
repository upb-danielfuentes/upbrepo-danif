# Funcion que retorne un listado de datos
ListaEmpleados = []

def empleados(nombre, salario, cargo, ano):
    ListaEmpleados.append(list((nombre,salario,cargo,ano)))
    return ListaEmpleados

def imprimirEmpleado(listaem):
    for i in listaem:
        print (f"El empleado {i[0]} tiene un salario de {i[1]} y es {i[2]} desde el año {i[3]}")

opcion = int(input("ingrese la opcion 1, 2, 3 "))

while opcion != 3:
    if opcion == 1:
        nombre = input("Ingrese el nombre: ")
        salario = float(input("Ingrese el salario: "))
        cargo = input("Ingrese el cargo: ")
        ano = int(input("Ingrese el año: "))
        emp = empleados(nombre, salario, cargo, ano)
    elif opcion == 2:
        imprimirEmpleado(emp)
    else:
        print("Opcion invalida")

    opcion = int(input("ingrese la opcion 1, 2, 3 "))

print("Fin del programa")