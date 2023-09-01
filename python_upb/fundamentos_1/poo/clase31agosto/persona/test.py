import unittest

class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        
    def imprimir(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nProfesión: {self.profesion}"
        
    def es_mayor_edad(self):
        return self.edad >= 18


class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona1 = Persona("Juan", 20, "Estudiante")
        self.persona2 = Persona("Maria", 17, "Estudiante")

    def test_imprimir(self):
        self.assertEqual(
            self.persona1.imprimir(),
            "Nombre: Juan\nEdad: 20\nProfesión: Estudiante"
        )

    def test_es_mayor_edad(self):
        self.assertTrue(self.persona1.es_mayor_edad())
        self.assertFalse(self.persona2.es_mayor_edad())


if __name__ == "__main__":
    unittest.main()
