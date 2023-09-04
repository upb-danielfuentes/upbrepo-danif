import unittest
from mi_agenda import Contacto, Agenda

class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
    
    def test_agregar_contacto(self):
        agenda = Agenda()
        contacto = Contacto("Juan", "123456789", "juan@example.com")
        agenda.agregar_contacto(contacto)
        self.assertIn(contacto, agenda.contactos)

if __name__ == "__main__":
    unittest.main()
