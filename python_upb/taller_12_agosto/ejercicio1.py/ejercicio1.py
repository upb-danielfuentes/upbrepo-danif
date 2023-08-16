# La UPB para liquidar el pago de la matricula de una estudiante le exige los siguiente datos:
# Numero inscripcion, nombres, patrimonio, estrato
# La universidad cobra un valor constante para cad estudiante de 50.000 , 
# Si el patrimonio es mayor de 2 millones y el estrato superior a 3
# Se le incrementa un porcentaje del 3% 

# Hacer un algoritmo que muestre: 
# Numero de inscripcion
# Nombres
# Pago de matricula

#Captura de Datos
numeroIncripcion = input("Ingrese el numero de inscripcion: ")
nombre = input("Ingrese su nombre: ")
patrimonio = float(input("Ingrese el valor de su patromonio:"))
estratoSocial = int(input("Ingrese su estrato social: "))
valorMatricula = 50000

if patrimonio > 2000000 and estratoSocial > 3:
    valorMatricula = valorMatricula + (patrimonio *0.03)

# Impresion del valor
print(f"El estudiante {nombre}, con codigo {numeroIncripcion} , debe pagar un valor de: ${valorMatricula} COP")
