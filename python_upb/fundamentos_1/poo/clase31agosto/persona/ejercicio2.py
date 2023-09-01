class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Profesión:", self.profesion)
        
    def es_mayor_edad(self):
        return self.edad >= 18


def main():
    personas = [
        Persona("Juan", 20, "Estudiante"),
        Persona("Maria", 17, "Estudiante")
    ]

    for idx, persona in enumerate(personas, start=1):
        print("Persona", idx)
        persona.imprimir()
        print("Es mayor de edad:", persona.es_mayor_edad())
        print()


if __name__ == "__main__":
    main()


