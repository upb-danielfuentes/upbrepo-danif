class Contacto:
    def __init__(self, nombre, telefono, email):
        self._nombre = nombre
        self._telefono = telefono
        self._email = email

    @property
    def nombre(self):
        return self._nombre

    @property
    def telefono(self):
        return self._telefono

    @property
    def email(self):
        return self._email


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def listar_contactos(self):
        for i, contacto in enumerate(self._contactos.values(), start=1):
            print(f"{i}. Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

    def obtener_contacto(self, nombre):
        return self._contactos.get(nombre)

    def actualizar_contacto(self, nombre, nuevo_contacto):
        if nombre in self._contactos:
            self._contactos[nombre] = nuevo_contacto
            print("Contacto actualizado con éxito.")
        else:
            print("Contacto no encontrado.")

    def eliminar_contacto(self, nombre):
        if nombre in self._contactos:
            contacto_eliminado = self._contactos.pop(nombre)
            print(f"Contacto eliminado: {contacto_eliminado.nombre}")
        else:
            print("Contacto no encontrado.")

def mostrar_menu():
    print("\n--- Menú de Contactos ---")
    print("1. Agregar Contacto")
    print("2. Listar Contactos")
    print("3. Obtener Contacto")
    print("4. Actualizar Contacto")
    print("5. Eliminar Contacto")
    print("6. Salir")

def main():
    agenda = Agenda()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            nuevo_contacto = Contacto(nombre, telefono, email)
            agenda.agregar_contacto(nuevo_contacto)
        elif opcion == "2":
            print("\nLista de Contactos:")
            agenda.listar_contactos()
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto que desea obtener: ")
            contacto = agenda.obtener_contacto(nombre)
            if contacto:
                print(f"Contacto: Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
            else:
                print("Contacto no encontrado.")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto que desea actualizar: ")
            telefono = input("Nuevo Teléfono: ")
            email = input("Nuevo Email: ")
            nuevo_contacto = Contacto(nombre, telefono, email)
            agenda.actualizar_contacto(nombre, nuevo_contacto)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
            agenda.eliminar_contacto(nombre)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
