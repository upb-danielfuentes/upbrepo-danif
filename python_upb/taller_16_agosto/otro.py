# Realice un algoritmo que capture los nombres de 5 personas

peopleName = []
peopleName.append(input('Ingrese el nombre de la primera persona: '))
peopleName.append(input('Ingrese el nombre de la segunda persona: '))
peopleName.append(input('Ingrese el nombre de la tercera persona: '))
peopleName.append(input('Ingrese el nombre de la cuarta persona: '))
peopleName.append(input('Ingrese el nombre de la quinta persona: '))

print('Lista de personas ingresadas')
print(peopleName)


# Realice un algoritmo que capture los nombres de x empleados 

employeesAmount = int(input('Ingrese la cantidad de empleados: '))
employeesName = []

for i in range(0, employeesAmount):
    peopleName.append(input(f'Ingrese el nombre del empleado {i + 1}: '))

print('Lista de empleados ingresados')
print(employeesName)