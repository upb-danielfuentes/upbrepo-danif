class Coche:
    def __init__(self, marca, modelo, anio, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0  # El coche se encuentra detenido

    def acelerar(self, velocidad):
        if 0 <= velocidad <= (self.velocidad_maxima - self.velocidad_actual):
            self.velocidad_actual += velocidad
        else:
            self.velocidad_actual = self.velocidad_maxima
        print(f"El coche aceleró a {self.velocidad_actual} km/h")

    def frenar(self, velocidad):
        if 0 <= velocidad <= self.velocidad_actual:
            self.velocidad_actual -= velocidad
        else:
            self.velocidad_actual = 0
        print(f"El coche frenó a {self.velocidad_actual} km/h")

    def obtener_informacion(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.anio}"

# Pruebas unitarias
import unittest

class TestCoche(unittest.TestCase):
    def setUp(self):
        self.mi_coche = Coche("Toyota", "Camry", 2020, 200)

    def test_acelerar(self):
        self.mi_coche.acelerar(50)
        self.assertEqual(self.mi_coche.velocidad_actual, 50)

    def test_frenar(self):
        self.mi_coche.acelerar(100)
        self.mi_coche.frenar(20)
        self.assertEqual(self.mi_coche.velocidad_actual, 80)

    def test_obtener_informacion(self):
        info = self.mi_coche.obtener_informacion()
        self.assertIn("Toyota", info)
        self.assertIn("Camry", info)
        self.assertIn("2020", info)

if __name__ == "__main__":
    unittest.main()
