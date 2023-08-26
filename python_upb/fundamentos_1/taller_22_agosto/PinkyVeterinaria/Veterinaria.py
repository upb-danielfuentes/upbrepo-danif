# CRUD
# Created - Crear un dato o crear un registro de información especifica 
# Read - Leer un dato almacenado o se encuentra dentro de nuestro sistema (busqueda de datos)
# Update - Modificar los datos y almacenar el cambio (cambiar)
# Delete - Eliminar el registro por completo del sistema
# Consulta para el sabado que son Tuplas, Set, Frozen...

# Sistema de información para una veterinaria
# Registrar pacientes --- Agregar los datos a una estructura --LISTO
# Registrar acompañante del paciente -- LISTO
# Crear una historia clinica 
# Calcular el valor de la consulta e imprimir factura - Pago 

print("SISTEMA DE VETERINARIA PINKY")

# Listas globales 
ListaAcom = []
ListaPacientes = []
ListaHistoria = []
ListaFactura = []

# Variables del paciente
pac_Nombre = ""
pac_Edad = 0
pac_Sexo = ""
pac_Peso = 0
pac_Raza = ""
pac_Raza_B = False

# Variables del acompañante
acom_Identificacion = ""
acom_NombreCompleto = ""
acom_Direccion = ""
acom_Telefono = ""
acom_Correo = ""

# Variables para la historia clinica
hist_Descripcion = ""

# Variables para la facturación
fac_ValorPago = 0

# Condicional de validación general
while True:
    verificacion = input("¿Desea agregar un paciente SI/NO? ")

    if verificacion.upper() == "SI":
        # Instrucciones del paciente nuevo
        ListaPacReg =[]
        ListaAcoReg = []

        # Id del acompañante
        acom_Identificacion = input("Ingrese el número de identificación del acompañante: ")
        while (acom_Identificacion == ""):
            print("!!Ingrese algún dato!!")
            acom_Identificacion = input("Ingrese el número de identificación del acompañante: ")
        
        # Nombre del paciente
        pac_Nombre = input("Ingrese el nombre del paciente: ")
        while (pac_Nombre == ""):
            print("!!Ingrese algún nombre!!")
            pac_Nombre = input("Ingrese el nombre del paciente: ")

        # Edad del paciente entre los valores de 0 y 20
        pac_Edad = int(input("Ingrese la edad del paciente (en años): "))
        while pac_Edad > 20 or pac_Edad <= 0:
            print("!!La edad del paciente esta incorrecta!!")
            pac_Edad = int(input("Ingrese la edad del paciente (en años): "))

        # Sexo del perro solo puede permitir Macho o Hembra
        pac_Sexo = input("Ingrese el sexo del paciente (MACHO/HEMBRA): ").upper()
        while pac_Sexo != "MACHO" and pac_Sexo != "HEMBRA":
            print("!!Error en el sexo!!")
            pac_Sexo = input("Ingrese el sexo del paciente (MACHO/HEMBRA): ").upper()
        
        # Peso se valida mayor que cero
        pac_Peso = float(input("Ingrese el peso del paciente (kilos): "))
        while (pac_Peso <= 0):
            print("!!Ingrese un valor valido!!")
            pac_Peso = float(input("Ingrese el peso del paciente (kilos): "))

        # Raza se convierte en un Booleano
        pac_Raza = input("¿El paciente es de raza? SI/NO ").upper()
        while (pac_Raza != "SI" and pac_Raza != "NO"):
            print("!!Ingrese un valor valido (SI/NO)!!")
            pac_Raza = input("¿El paciente es de raza? SI/NO ").upper()
        else:
            if pac_Raza == "SI":
                pac_Raza_B = True
            elif pac_Raza == "NO":
                pac_Raza_B = False
        
        ListaPacReg=list((acom_Identificacion, pac_Nombre, pac_Edad, pac_Sexo, pac_Peso, pac_Raza_B))
        ListaPacientes.append(ListaPacReg)

        # Continuamos con los datos del acompañante 
        acom_NombreCompleto = input(f"Ingrese el nombre del acompañante de {pac_Nombre}: ")
        while (acom_NombreCompleto == ""):
            print("!!Ingrese algún nombre de acompañante!!")
            acom_NombreCompleto = input(f"Ingrese el nombre del acompañante de {pac_Nombre}: ")

        acom_Direccion = input("Ingrese la dirección del acompañante: ")
        while (acom_Direccion == ""):
            print("!!Ingrese alguna dirección del acompañante!!")
            acom_Direccion = input("Ingrese la dirección del acompañante: ")

        acom_Telefono = input("Ingrese un teléfono de contacto: ")
        while (acom_Telefono == ""):
            print("!!Ingrese un número de teléfono de contacto!!")
            acom_Telefono = input("Ingrese un teléfono de contacto: ")

        acom_Correo = input("Ingrese un correo electrónico: ")
        val_Correo = list(acom_Correo)
        while val_Correo.count("@") != 1:
            print("¡¡Error en el formato de correo electrónico!!")
            acom_Correo = input("Ingrese un correo electrónico: ")
            val_Correo = list(acom_Correo)

        ListaAcoReg = list((acom_Identificacion, acom_NombreCompleto, acom_Direccion, acom_Telefono, acom_Correo))
        ListaAcom.append(ListaAcoReg)
        
        print("---------------------------------")
        print("Lista de pacientes registrados")
        print(ListaPacientes)
        print("---------------------------------")
        print("Lista de acompañantes registrados")
        print(ListaAcom)
        print("---------------------------------")

    else:
        if verificacion.upper() == "NO":
            # Instrucciones del paciente existente
            #hacia el siguiente instruccion por fuera del while
            verificacion2 = int(input("Elija la opción que desee: \n1. Agregar Historia Clinica \n2. Facturar Consulta \n3. Finalizar el programa \nIngrese la opción: "))
            while verificacion2 != 1 and verificacion2 != 2 and verificacion2 != 3:
                print("Opción elegida incorrecta. Intentelo de nuevo")
                verificacion2 = int(input("Elija la opción que desee: \n1. Agregar Historia Clinica \n2. Facturar Consulta \n3. Finalizar el programa"))

            if verificacion2 == 1:
                #Agregar una historia clinica
                id_acomp = input("Ingrese el número de identificación del acompañante: ")
                while id_acomp == "":
                    print("¡¡Debe ingresar un ID para agregar la historia!!")
                    id_acomp = input("Ingrese el número de identificación del acompañante: ")

                banderita = False

                for i in ListaPacientes:
                    x = i[0]
                    if x == id_acomp:
                        banderita = True
                
                if banderita:
                    ListaHistReg =[]
                    hist_Descripcion = input("Describa el estado del paciente: ")
                    while hist_Descripcion == "":
                        print("¡¡Debe agregar una historia!!")
                        hist_Descripcion = input("Describa el estado del paciente: ")
                    
                    ListaHistReg = list((id_acomp, hist_Descripcion))
                    ListaHistoria.append(ListaHistReg)
                    print(ListaHistoria)
                else:
                    print("No existe el ID del acompañante")
            elif verificacion2 == 2:
                 #Facturar consulta
                id_acomp = input("Ingrese el número de identificación del acompañante: ")
                while id_acomp == "":
                    print("¡¡Debe ingresar un ID para agregar la historia!!")
                    id_acomp = input("Ingrese el número de identificación del acompañante: ")

                banderita = False

                for i in ListaPacientes:
                    x = i[0]
                    if x == id_acomp:
                        banderita = True
                
                if banderita:
                    ListaFacReg = []
                    # Valor de la hora de mi medico es de $20.000
                    cantHora = float(input("¿Cuántas horas se quedo el paciente en la Veterinaria? "))
                    fac_ValorPago = cantHora * 20000
                    ListaFacReg = list((id_acomp, fac_ValorPago))
                    ListaFactura.append(ListaFacReg)

                    # Imprimimos la factura del cliente
                    # banderita1 = False
                    # banderita2 = False
                    # banderita3 = False

                    paciente, acompanante, historia = "", "", ""

                    for a in ListaPacientes:
                        pac = a[0]
                        if pac == id_acomp:
                            #banderita1 = True
                            paciente = a[1]
                    
                    for b in ListaAcom:
                        acom = b[0]
                        if acom == id_acomp:
                            #banderita2 = True
                            acompanante = b[1]

                    for c in ListaHistoria:
                        hist = c[0]
                        if hist == id_acomp:
                            #banderita3 = True
                            historia = c[1]
                    
                    print(f"FACTURA DE {acompanante.upper()}")
                    print(f"El paciente {paciente.upper()} por el caso presentado en la historia clinica que describe: {historia}")
                    print(f"Debe pagar un valor de ${fac_ValorPago:,}")


            elif verificacion2 == 3:
                #Salir del programa
                break
            
        else:
            print("¡¡¡El valor ingresado es erroneo!!! Intentelo de nuevo")

print("FIN DEL PROGRAMA")