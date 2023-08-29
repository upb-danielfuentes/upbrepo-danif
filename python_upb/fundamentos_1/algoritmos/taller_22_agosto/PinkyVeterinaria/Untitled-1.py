

class Paciente:
    def __init__(self, cedula, nombre, fecha_nacimiento, genero, telefono, correo):
        self.cedula = cedula
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.telefono = telefono
        self.correo = correo
        self.odontologo = None
        self.citas = 0

class Odontologo:
    def __init__(self, nombre, costo_consulta, max_citas, atiende_mujeres):
        self.nombre = nombre
        self.costo_consulta = costo_consulta
        self.max_citas = max_citas
        self.atiende_mujeres = atiende_mujeres
        self.citas_realizadas = 0

def dar_bienvenida():
    print("Bienvenido al sistema de Odontología Mi Mueca")

def registrar_pacientes(cantidad):
    pacientes = []
    for _ in range(cantidad):
        cedula = input("Ingrese la cédula del paciente: ")
        nombre = input("Ingrese el nombre completo del paciente: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente: ")
        genero = input("Ingrese el género del paciente (F/M): ")
        telefono = input("Ingrese el teléfono del paciente: ")
        correo = input("Ingrese el correo electrónico del paciente: ")
        pacientes.append(Paciente(cedula, nombre, fecha_nacimiento, genero, telefono, correo))
    return pacientes

def asignar_odontologo(paciente, odontologos):
    for odontologo in odontologos:
        if (odontologo.atiende_mujeres and paciente.genero == 'F') or (not odontologo.atiende_mujeres and paciente.genero == 'M'):
            if paciente.citas < odontologo.max_citas:
                paciente.odontologo = odontologo
                paciente.citas += 1
                odontologo.citas_realizadas += 1
                return

def mostrar_factura(paciente):
    print("Factura para:", paciente.nombre)
    print("Médico asignado:", paciente.odontologo.nombre)
    print("Valor a pagar por consulta:", paciente.odontologo.costo_consulta)
    print()

def mostrar_total_pagos(odontologos):
    for odontologo in odontologos:
        print("Total de pagos para", odontologo.nombre + ":", odontologo.citas_realizadas * odontologo.costo_consulta)
    print()

def despedida():
    print("Gracias por utilizar el sistema de Odontología Mi Mueca. ¡Hasta pronto!")

def main():
    dar_bienvenida()

    cant_pacientes = int(input("Ingrese la cantidad de pacientes a registrar: "))
    pacientes = registrar_pacientes(cant_pacientes)

    odontologo1 = Odontologo("Doctor Santo Grial", 180000, 5, True)
    odontologo2 = Odontologo("Doctor Ariel Mercado", 90000, float('inf'), False)
    odontologos = [odontologo1, odontologo2]

    for paciente in pacientes:
        asignar_odontologo(paciente, odontologos)

    for paciente in pacientes:
        mostrar_factura(paciente)

    mostrar_total_pagos(odontologos)

    despedida()

if __name__ == "__main__":
    main()
