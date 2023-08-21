# Realice un algoritmo que permita el registro de 5 pacientes con los
# siguientes campos: nombre, apellido, telefono, fecha de nacimiento
# sexo , correo electronico, direccion, ciudad, pais, estado civil
# este debe permitir distinguir entre las mujeres y hombres registrados
# y que adicional permita mostrar las siguientes sugerencias segun la edad
# 1. Si es menor de edad y mujer , se deben aplicar la vacuna de tetanos
# 2. 
# 3.
# 4. Si es hombre menor de edad que se aplique la vacuna de la influenza
# 5. Si es hombre de 18 a 30 años que ese aplique la vacuna de tetanos
# 6. Si es hombre mayor de 40 años que la indique que se haga el examen de prostata

def pacientes():
    try:
        pacientes = []
        for i in range(0,5):
            nombre = input("Ingrese el nombre del paciente: ")
            apellido = input("Ingrese el apellido del paciente: ")
            telefono = input("Ingrese el telefono del paciente: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente: ")
            sexo = input("Ingrese el sexo del paciente: ")
            correo = input("Ingrese el correo electronico del paciente: ")
            direccion = input("Ingrese la direccion del paciente: ")
            ciudad = input("Ingrese la ciudad del paciente: ")
            pais = input("Ingrese el pais del paciente: ")
            estado_civil = input("Ingrese el estado civil del paciente: ")
            pacientes.append({"nombre":nombre,"apellido":apellido,"telefono":telefono,"fecha_nacimiento":fecha_nacimiento,"sexo":sexo,"correo":correo,"direccion":direccion,"ciudad":ciudad,"pais":pais,"estado_civil":estado_civil})
        for i in pacientes:
            if i["sexo"] == "femenino" and i["edad"] < 18:
                print(f"La paciente {i['nombre']} {i['apellido']} debe aplicarse la vacuna de tetanos")
            elif i["sexo"] == "masculino":
                if i["edad"] < 18:
                    print(f"El paciente {i['nombre']} {i['apellido']} debe aplicarse la vacuna de influenza")
                elif i["edad"] >= 18 and i["edad"] <= 30:
                    print(f"El paciente {i['nombre']} {i['apellido']} debe aplicarse la vacuna de tetanos")
                elif i["edad"] > 40:
                    print(f"El paciente {i['nombre']} {i['apellido']} debe realizarse el examen de prostata")
    except ValueError as e:
        print("Error en el algoritmo",e)
pacientes()