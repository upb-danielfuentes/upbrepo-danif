class PetChipinShop:
    def __init__(self):
        self.mascotas = []
        self.horarios_disponibles = ["09:00", "10:00", "11:00", "15:00", "16:00", "17:00"]

    def pet_chipin_shop(self):
        print("Bienvenido a PetChipinShop, la veterinaria para tus mascotas.")

        print("\n¿Qué acción deseas realizar?")
        print("1. Agendar una cita")
        print("2. Ver citas agendadas")
        print("3. Salir")
        opcion = int(input())

        if opcion == 1:
            self.agendar_cita()
        elif opcion == 2:
            self.ver_citas_agendadas()
        elif opcion == 3:
            print("¡Gracias por visitar PetChipinShop!")
            return
        else:
            print("Opción no válida")

    def agendar_cita(self):
        print("Ingrese el nombre de la mascota:")
        nombre_mascota = input()
        self.mascotas.append(nombre_mascota)

        print("Horarios disponibles:")
        for i, horario in enumerate(self.horarios_disponibles, start=1): # enumerate() es una función que devuelve una tupla con el índice y el elemento de una lista
            print(f"{i}. {horario}")
        
        num_horario = int(input("Ingrese el número del horario deseado: "))
        if 1 <= num_horario <= len(self.horarios_disponibles):
            horario_elegido = self.horarios_disponibles.pop(num_horario - 1)
            print(f"Cita agendada para {nombre_mascota} a las {horario_elegido}")
        else:
            print("Opción de horario no válida")

    def ver_citas_agendadas(self):
        print("Citas agendadas:")
        for mascota in self.mascotas:
            print("Mascota:", mascota)

if __name__ == "__main__":
    pet_chipin_shop = PetChipinShop()
    pet_chipin_shop.pet_chipin_shop()
