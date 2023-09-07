import mysql.connector

# Clase para la gestión de la conexión
class ConexionMySQL:
    def __init__(self, usuario, contraseña, host, base_de_datos):
        self.config = {
            'user': usuario,
            'password': contraseña,
            'host': host,
            'database': base_de_datos,
        }
        self.conexion = None

    def conectar(self):
        self.conexion = mysql.connector.connect(**self.config)

    def cerrar(self):
        if self.conexion:
            self.conexion.close()

# Clase para Insertar (CREATE)
class InsertarEstudiante:
    def __init__(self, conexion):
        self.conexion = conexion

    def ejecutar(self, id_estudiante, nombre, edad):
        cursor = self.conexion.cursor()
        consulta = "INSERT INTO estudiante (id, nombre, edad) VALUES (%s, %s, %s)"
        datos = (id_estudiante, nombre, edad)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        cursor.close()

# Clase para Actualizar (UPDATE)
class ActualizarEstudiante:
    def __init__(self, conexion):
        self.conexion = conexion

    def ejecutar(self, id_estudiante, nuevo_nombre, nueva_edad):
        cursor = self.conexion.cursor()
        consulta = "UPDATE estudiante SET nombre = %s, edad = %s WHERE id = %s"
        datos = (nuevo_nombre, nueva_edad, id_estudiante)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        cursor.close()

# Clase para Eliminar (DELETE)
class EliminarEstudiante:
    def __init__(self, conexion):
        self.conexion = conexion

    def ejecutar(self, id_estudiante):
        cursor = self.conexion.cursor()
        consulta = "DELETE FROM estudiante WHERE id = %s"
        cursor.execute(consulta, (id_estudiante,))
        self.conexion.commit()
        cursor.close()

# Clase para Consultar (READ)
class ConsultarEstudiantes:
    def __init__(self, conexion):
        self.conexion = conexion

    def ejecutar(self):
        cursor = self.conexion.cursor()
        consulta = "SELECT * FROM estudiante"
        cursor.execute(consulta)
        registros = cursor.fetchall()
        cursor.close()
        return registros

def main():
    # Solicitar información al usuario
    usuario = input("Ingrese su nombre de usuario MySQL: ")
    contraseña = input("Ingrese su contraseña MySQL: ")
    host = input("Ingrese el nombre de host MySQL (por defecto, localhost): ") or "localhost"
    
    conexion_db = ConexionMySQL(usuario, contraseña, host, 'upb')
    conexion_db.conectar()

    while True:
        print("\nOpciones:")
        print("1. Agregar un nuevo estudiante")
        print("2. Actualizar un estudiante existente")
        print("3. Eliminar un estudiante existente")
        print("4. Consultar todos los estudiantes")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción que desee: ")

        if opcion == "1":
            id_estudiante = int(input("Ingrese el ID del estudiante: "))
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = int(input("Ingrese la edad del estudiante: "))

            insertar = InsertarEstudiante(conexion_db.conexion)
            insertar.ejecutar(id_estudiante, nombre, edad)
            print("Registro de estudiante insertado correctamente.")

        elif opcion == "2":
            id_estudiante = int(input("Ingrese el ID del estudiante que desea actualizar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre del estudiante: ")
            nueva_edad = int(input("Ingrese la nueva edad del estudiante: "))

            actualizar = ActualizarEstudiante(conexion_db.conexion)
            actualizar.ejecutar(id_estudiante, nuevo_nombre, nueva_edad)
            print("Registro de estudiante actualizado correctamente.")

        elif opcion == "3":
            id_estudiante = int(input("Ingrese el ID del estudiante que desea eliminar: "))

            eliminar = EliminarEstudiante(conexion_db.conexion)
            eliminar.ejecutar(id_estudiante)
            print("Registro de estudiante eliminado correctamente.")

        elif opcion == "4":
            consultar = ConsultarEstudiantes(conexion_db.conexion)
            registros = consultar.ejecutar()
            for registro in registros:
                print(registro)

        elif opcion == "5":
            break

    conexion_db.cerrar()

if __name__ == "__main__":
    main()
