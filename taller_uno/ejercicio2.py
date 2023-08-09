# Algoritmo Dos

def calcular_salario_mensual():
    # Datos del empleado
    va = 15000
    print ("Bienvenidos a SancochoFood Company S.A")
    nombre_cliente = input("Ingrese el nombre del empleado: ")
    hs = float(input("Ingrese la cantidad de horas que trabaja en la semana: "))
    
    # Cálculo del salario sin deducciones
    salario_sin_deducciones = va * hs * 4  # Se multiplican las horas por 4 semanas al mes
    
    # Cálculo de deducciones
    deduccion_salud = salario_sin_deducciones * 0.04
    deduccion_pension = salario_sin_deducciones * 0.04
    deduccion_caja_compensacion = salario_sin_deducciones * 0.02
    auxilio_transporte = 140606
    
    # Cálculo del salario mensual real
    salario_mensual = salario_sin_deducciones - deduccion_salud - deduccion_pension - deduccion_caja_compensacion + auxilio_transporte

    # Mostrar resultados
    print("\nResultado:")
    print("Salario mensual sin deducciones: COP", salario_sin_deducciones)
    print("Deducción por salud: COP", deduccion_salud)
    print("Deducción por pensión: COP", deduccion_pension)
    print("Deducción por caja de compensación: COP", deduccion_caja_compensacion)
    print("Auxilio de transporte: COP", auxilio_transporte)
    print("El Salario mensual real neto que recibirias en tu cuenta bancaria", nombre_cliente, "seria de: COP", salario_mensual)


# Ejecutar el programa
calcular_salario_mensual()
