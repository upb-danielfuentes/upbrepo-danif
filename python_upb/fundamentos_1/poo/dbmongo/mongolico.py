import pymongo

# Conecta a MongoDB (asegúrate de que MongoDB esté ejecutándose en el puerto predeterminado 27017)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Crea una base de datos llamada "mi_db"
db = client["mi_db"]

# Crea una colección llamada "estudiantes"
estudiantes = db["estudiantes"]

# Función para crear un nuevo estudiante
def crear_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    estudiante = {"nombre": nombre, "edad": edad}
    estudiantes.insert_one(estudiante)
    print(f"Estudiante {nombre} creado con éxito.")

# Función para leer todos los estudiantes
def obtener_estudiantes():
    return list(estudiantes.find())

# Función para obtener un estudiante por nombre
def obtener_estudiante_por_nombre():
    nombre = input("Ingrese el nombre del estudiante que desea buscar: ")
    estudiante = estudiantes.find_one({"nombre": nombre})
    if estudiante:
        print(estudiante)
    else:
        print(f"No se encontró ningún estudiante con el nombre {nombre}.")

# Función para actualizar la edad de un estudiante por nombre
def actualizar_edad():
    nombre = input("Ingrese el nombre del estudiante que desea actualizar: ")
    nueva_edad = int(input("Ingrese la nueva edad del estudiante: "))
    estudiantes.update_one({"nombre": nombre}, {"$set": {"edad": nueva_edad}})
    print(f"Edad del estudiante {nombre} actualizada con éxito.")

# Función para eliminar un estudiante por nombre
def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante que desea eliminar: ")
    estudiantes.delete_one({"nombre": nombre})
    print(f"Estudiante {nombre} eliminado con éxito.")

# Ciclo principal
while True:
    print("\nOpciones:")
    print("1. Crear estudiante")
    print("2. Leer estudiantes")
    print("3. Buscar estudiante por nombre")
    print("4. Actualizar edad del estudiante")
    print("5. Eliminar estudiante")
    print("6. Salir")
    
    opcion = input("Ingrese el número de la opción que desea realizar: ")
    
    if opcion == "1":
        crear_estudiante()
    elif opcion == "2":
        print("Estudiantes:")
        estudiantes_list = obtener_estudiantes()
        for estudiante in estudiantes_list:
            print(estudiante)
    elif opcion == "3":
        obtener_estudiante_por_nombre()
    elif opcion == "4":
        actualizar_edad()
    elif opcion == "5":
        eliminar_estudiante()
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
