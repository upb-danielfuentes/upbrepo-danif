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

def veterinaria():
    listaPacientesTotal = []
    listaAcompañanteTotal = []
    listaHistoriaClinicaTotal = []
    listaFacturaTotal = []

    while True:
        verificacion = input("Desea agregar un paciente? SI/NO: ")
        if verificacion.upper() == "SI":
            acomIdentificacion = input_texto("Ingrese el ID del Dueño (10 caracteres): ")
            while len(acomIdentificacion) != 10:
                print("El ID debe tener 10 caracteres")
                acomIdentificacion = input_texto("Ingrese el ID del Dueño (10 caracteres): ")
           
            pacNombre = input_texto("Ingrese el nombre del paciente: ")
            pacEdad = input_entero("Ingrese la edad del paciente: ")
            while pacEdad < 0 or pacEdad > 20:
                print("La edad debe estar entre 0 y 20 años")
                pacEdad = input_entero("Ingrese la edad del paciente: ")

            pacSexo = input("Ingrese el sexo del paciente (M/F): ").upper()
            while pacSexo != "M" and pacSexo != "F":
                print("El sexo debe ser M o F")
                pacSexo = input("Ingrese el sexo del paciente: ").upper()

            pacPeso = float(input("Ingrese el peso del paciente: "))
            while pacPeso <= 0:
                print("El peso debe ser mayor a 0")
                pacPeso = float(input("Ingrese el peso del paciente: "))

            pacRaza_Boo = False
            pacRaza = input("El paciente es de raza (SI/NO): ").upper()
            while pacRaza != "SI" and pacRaza != "NO":
                print("La respuesta debe ser SI o NO")
                pacRaza = input("El paciente es de raza (SI/NO): ").upper()
            if pacRaza == "SI":
                pacRaza_Boo = True
            elif pacRaza == "NO":
                pacRaza_Boo = False

            listaPacientesReg = [acomIdentificacion, pacNombre, pacEdad, pacSexo, pacPeso, pacRaza_Boo]
            listaPacientesTotal.append(listaPacientesReg)

            acomNombre = input_texto("Ingrese el nombre del acompañante: ")
            acomDireccion = input_texto("Ingrese la dirección del acompañante: ")
            acomTelefono = input_entero("Ingrese el teléfono del acompañante: ")
            acomCorreo = input_texto("Ingrese el correo del acompañante: ")
            while "@" not in acomCorreo:
                print("El correo debe contener un @")
                acomCorreo = input_texto("Ingrese el correo del acompañante: ")

            listaAcompañanteReg = [acomNombre, acomDireccion, acomTelefono, acomCorreo]
            listaAcompañanteTotal.append(listaAcompañanteReg)
            
        elif verificacion.upper() == "NO":
            verificacion2 = input("Elija la opción que desee realizar (1: Agregar HC) / (2: No Agregar HC) / (3: Salir): ")
            
            while verificacion2 not in ["1", "2", "3"]:
                print("La respuesta debe ser 1, 2 o 3")
                verificacion2 = input("Elija la opción que desee realizar (1: Agregar HC) / (2: No Agregar HC) / (3: Salir): ")

            if verificacion2 == "1":
                acomIdentificacion = input_texto("Ingrese el ID del acompañante: ")

                banderita = False
                
                for i in listaPacientesTotal:
                    x = i[0]
                    if x == acomIdentificacion:
                        banderita = True
                        print("El ID ya existe")
                        break
                        
                if banderita:
                    historiaClinica = input_texto("Ingrese la historia clínica: ")
                    listaHistoriaClinicaReg = [acomIdentificacion, historiaClinica]
                    listaHistoriaClinicaTotal.append(listaHistoriaClinicaReg)
                    print("La historia clínica se ha agregado correctamente")

            elif verificacion2 == "2":
                acomIdentificacion = input_texto("Ingrese el ID del acompañante: ")
                banderita = False
                for i in listaPacientesTotal:
                    x = i[0]
                    if x == acomIdentificacion:
                        banderita = True
                if banderita:
                    factura = input_texto("Ingrese la factura: ")
                    fac_ValorPago = cantHora * 20000
                    listaFacturaReg = [acomIdentificacion, factura]
                    listaFacturaTotal.append(listaFacturaReg)
                    print("La factura se ha agregado correctamente")

                    paciente, acomp, historia = "", "", ""

                    for a in listaPacientesTotal:
                        pac = a[0]
                        if pac == acomIdentificacion:
                            paciente = a[1]

                    for b in listaAcompañanteTotal:
                        pac = b[0]
                        if pac == acomIdentificacion:
                            acomp = b[1]

                    for c in listaHistoriaClinicaTotal:
                        pac = c[0]
                        if pac == acomIdentificacion:
                            historia = c[1]

                    print("Factura de pago")
                    print("Paciente: ", paciente)
                    print("Acompañante: ", acomp)
                    print("Historia Clínica: ", historia)
                    print("Valor a pagar: ", fac_ValorPago)
                    
            elif verificacion2 == "3":
                print("Hasta pronto")
                break

            print("Estos fueron todos los datos ingresados:")
            print(listaPacientesTotal)
            print(listaAcompañanteTotal)
            print(listaHistoriaClinicaTotal)
            break
        else:
            print("La respuesta debe ser SI o NO")
            continue

veterinaria()