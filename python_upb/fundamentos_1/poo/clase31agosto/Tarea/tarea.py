class GestorDeTareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, indice):
        if 1 <= indice <= len(self.tareas):
            tarea_eliminada = self.tareas.pop(indice - 1)
            return tarea_eliminada
        else:
            return None

    def mostrar_tareas(self):
        for i, valor in enumerate(self.tareas, start=1):
            print(f"{i}. {valor}")

    def obtener_tarea(self, indice):
        if 1 <= indice <= len(self.tareas):
            return self.tareas[indice - 1]
        else:
            return None

    def actualizar_tarea(self, indice, nueva_tarea):
        if 1 <= indice <= len(self.tareas):
            self.tareas[indice - 1] = nueva_tarea

def mostrar_menu():
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar Tarea")
    print("2. Eliminar Tarea")
    print("3. Mostrar todas las Tareas")
    print("4. Obtener una Tarea de la lista")
    print("5. Actualizar Tarea")
    print("6. Salir de las Tareas")

def main():
    gestor = GestorDeTareas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción:")

        if opcion == "1":
            tarea = input("Agregue la nueva tarea: ")
            gestor.agregar_tarea(tarea)
        elif opcion == "2":
            indice = int(input("Ingrese el índice de la tarea que desea eliminar: "))
            tarea_eliminada = gestor.eliminar_tarea(indice)
            if tarea_eliminada is not None:
                print(f"Tarea eliminada: {tarea_eliminada}")
            else:
                print("La tarea no existe.")
        elif opcion == "3":
            print("\nLISTADO DE TAREAS:")
            gestor.mostrar_tareas()
        elif opcion == "4":
            indice = int(input("Ingrese el índice de la tarea que desea ver: "))
            tarea_obtenida = gestor.obtener_tarea(indice)
            if tarea_obtenida is not None:
                print(f"Tarea {indice}: {tarea_obtenida}")
            else:
                print("La tarea no existe.")
        elif opcion == "5":
            indice = int(input("Ingrese el índice de la tarea que desea actualizar: "))
            tarea_mod = input("Ingrese la nueva tarea para reemplazar: ")
            gestor.actualizar_tarea(indice, tarea_mod)
            print("Tarea actualizada con éxito.")
        elif opcion == "6":
            print("Saliendo del programa....")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
