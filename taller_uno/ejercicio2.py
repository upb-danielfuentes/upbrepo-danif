# Un empleado de la empresa SancochoFood desea saber cual es su salario real, teniendo 
# presente los descuentos que se aplican por las diferentes deducciones legales. El empleado 
# solo conoce cual es el valor de su hora ($15.000) y la cantidad de horas que trabaja por 
# semana, el sistema se la debe solicitar al empleado que ingrese cuantas horas trabajo a la 
# semana. Realice el cálculo del salario del empleado al mes, sabiendo que para salud se le 
# deduce el 4%, para pensión le deduce el 4%, para caja de compensación el 2% y le agrega el 
# auxilio de transporte que es un valor fijo para los Colombianos de $140.606.
# Es importante que le indique al empleado el valor de su salario mensual, el valor que le 
# deducen por salud, el valor que le deducen por pensión, el valor que le deducen por caja de 
# compensación y el valor que le adicionan por auxilio de transporte, finalmente le indicamos 
# el valor que será consignado en la cuenta.

def calcular_salario_mensual():
    # Datos del empleado
    valor_hora = 15000
    horas_semana = float(input("Ingrese la cantidad de horas que trabaja por semana: "))
    
    # Cálculo del salario sin deducciones
    salario_sin_deducciones = valor_hora * horas_semana * 4  # Se multiplican las horas por 4 semanas al mes
    
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
    print("Salario mensual real: COP", salario_mensual)


# Ejecutar el programa
calcular_salario_mensual()
