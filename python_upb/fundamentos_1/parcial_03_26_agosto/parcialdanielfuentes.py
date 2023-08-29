'''
La odontologia Mi Mueca desea agregar un sistema de informacion que los ayude a gesitonar los
pacientes atentidos por dia, para ellos requiere iniciar un sistema que permita hacer lo siguiente:
1. Dar la bienvenida al sistema
2. Registrar sus pacientes en el sistema con cedula, nombre completo, fecha de nacimiento, genero (F/M), telefono y correo electronico.
2.1 La cantidad de pacientes a registrar va a depender de la secretaria de la odontologia, por lo tanto se le debe indicar que escriba la cantidad
3. Asignarles el odontologo que los va a atender y la cantida de citas que requiere con el.
Los odontoogos disponibles son: 
a. Doctor Santo Grial con costo por consulta de $ 180.000 y no atiende un mismo paciente mas de 5 veces
b. Doctor Ariel Mercado con costo por consulta de $ 90.000 y solo le gusta atender mujeres no hombres
4. Mostrarles el nombre del titular de la factura, el valor a pagar por las consultas y el medico que asignaron para sus citas.
5. Mostrar total de pagos por citas por medico
6. Finalizar el programa con despedida

Importante : Siempre permitir ver impresos por pantalla todos los pacientes, las opciones de odontologos y las factuas generadas por los clientes

'''

ListaPacientesOdonto = []
ListaMedicoOdonto = []
ListaFactura = []

idPaciente = ""
nombrePaciente = ""
fechaNacimientoPaciente = ""
generoPaciente = ""
telefonoPaciente = ""
emailPaciente = ""


def input_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("El valor debe ser mayor a 0")
            else:
                return valor
        except ValueError:
            print("Ingrese un valor numérico válido")

def input_texto(mensaje):
    while True:
        valor = input(mensaje)
        if valor.strip() == "":
            print("Este campo no puede estar vacío")
        else:
            return valor

def mimueca():

    print("--------------------------------------------------")
    print("🚀 Iniciando programa 🚀")
    input("Bienvenidos a Odontologia Mi Mueca, presione Enter para continuar...")
    print("--------------------------------------------------")
    while True:

        checkuno = input("¿Desea registar pacientes SI/NO? ")
        
        if checkuno.upper() == "SI":
                
            cantPacientes = input_entero("Ingrese la cantidad de pacientes a registrar: ")
            for i in range(cantPacientes):
                
                print("--------------------------------------------------")
                print (f"Estas a punto de ingresa {i+1} de {cantPacientes} pacientes")
                
                ListaPacientesRegistro = []
                # Id Paciente
                idPaciente = input_texto("Ingrese el ID del Paciente (2 caracteres): ")                
                while len(idPaciente) != 2:
                    print("El ID debe tener 2 caracteres")
                    idPaciente = input_texto("Ingrese el ID del Paciente (2 caracteres): ")
                    
                # Nombre Paciente
                nombrePaciente = input_texto("Ingrese el nombre del paciente: ")
                    
                # Fecha de Nacimiento
                fechaNacimientoPaciente = input_entero("Ingrese la fecha de nacimiento del paciente: ")
                    
                # Genero(F/M)
                generoPaciente = input_texto("Ingrese el genero del paciente (M/H): ").upper()
                while generoPaciente != "M" and generoPaciente != "H":
                    print("!! Error en el sexo !!")
                    generoPaciente = input("Ingrese nuevamente el genero del paciente (M/H): ").upper()
                    
                # Telefono
                telefonoPaciente = input_entero("Ingrese el telefono del paciente: ")
                    # Email
                    
                emailPaciente= input_texto("Ingrese el email del paciente: ")
                val_Correo = list(emailPaciente)
                while val_Correo.count("@") != 1:
                    print("¡¡Error en el formato de correo electrónico!!")
                    emailPaciente = input("Ingrese un correo electrónico valido: ")
                    val_Correo = list(emailPaciente)

                ListaPacientesRegistro = list((idPaciente, nombrePaciente, fechaNacimientoPaciente, generoPaciente, telefonoPaciente, emailPaciente))
                ListaPacientesOdonto.append(ListaPacientesRegistro)

        else:
            if checkuno.upper() == "NO":
                # Cuando ya existe un paciente registrado
                checkdos = int(input("Elija la opción que desee realizar: \n1. Asignar Odontologo \n2. Mostrar Total Pagos \n3. Finalizar el programa \n Ingrese una opción: "))
                while checkdos != 1 and checkdos != 2 and checkdos != 3:
                    print("Opción elegida incorrecta. Intentelo de nuevo")
                    checkdos = int(input("Elija la opción que desee realizar: \n1. Asignar Odontologo \n2. Mostrar Total Pagos \n3. Finalizar el programa \n Ingrese una opción: "))

            if checkdos == 1:
                #Agregar la cantidad de citas que requiere el paciente
                print("A que paciente la vas a asignar doctor?: ")
                print(ListaPacientesOdonto)
                idPacienteRegistrado = input_texto("Ingrese el ID del paciente registrado: ")
                print("--------------------------------------------------")
                banderita = False
                for i in ListaPacientesOdonto:
                    x = i[0]
                    if x == idPacienteRegistrado:
                        banderita = True

                cantidaCitas = input_entero("Ingrese la cantidad de citas que requiere el paciente: ")
                if banderita:
                    print ("Doctores disponibles para la cita: ")
                    print("--------------------------------------------------")
                    print("1. Doctor Santo Grial")
                    print("2. Doctor Ariel Mercado")
                    print("--------------------------------------------------")
                    doctor = input_texto("Ingrese el numero del doctor que desea: ").upper()
                    while doctor != "1" and doctor != "2":
                        print("!! Error en el numero del doctor !!")
                        doctor = input("Ingrese nuevamente el numero del doctor que desea: ").upper()
                    if doctor == "1":
                        if cantidaCitas <= 5:
                            print("--------------------------------------------------")
                            print("Factura del paciente")
                            print("--------------------------------------------------")
                            print("Nombre del paciente: ", nombrePaciente)
                            print("Valor a pagar por cada consulta: $ 180.000")
                            print("Doctor asignado: ", doctor)
                            print("--------------------------------------------------")
                            ListaFacturaRegistro = list((idPacienteRegistrado, nombrePaciente, cantidaCitas*180000, doctor))
                            ListaFactura.append(ListaFacturaRegistro)
                            print("--------------------------------------------------")
                            print("Lista de facturas generadas")
                            print(ListaFactura)
                            print("--------------------------------------------------")
                        else:
                            print("El doctor Santo Grial tiene la agenda llena en este momento")
                    elif doctor == "2":
                        if generoPaciente == "M":
                            print("El doctor Ariel Mercado tiene la agenda llena en este momento")
                        else:
                            print("--------------------------------------------------")
                            print("Factura del paciente")
                            print("--------------------------------------------------")
                            print("Nombre del paciente: ", nombrePaciente)
                            print("Valor a pagar por la consulta: $ 90.000")
                            print("Doctor asignado: ", doctor)
                            print("--------------------------------------------------")
                            ListaFacturaRegistro = list((idPacienteRegistrado, nombrePaciente, cantidaCitas*90000, doctor))
                            ListaFactura.append(ListaFacturaRegistro)
                            print("--------------------------------------------------")
                            print("Lista de facturas generadas")
                            print(ListaFactura)
                            print("--------------------------------------------------")

                else:
                    print("No existe el ID del acompañante")
                                 
            elif checkdos == 2:
                #Mostrar el total de pagos por citas por medico
                print("--------------------------------------------------")
                print("Lista de facturas generadas")
                
                print("--------------------------------------------------")
                break
            elif checkdos == 3:
                #Salir del programa
                break
           
mimueca()