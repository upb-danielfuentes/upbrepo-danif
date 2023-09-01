import pytest

from tarea import GestorDeTareas

@pytest.fixture
def gestor():
    return GestorDeTareas()

def test_agregar_tarea(gestor):
    gestor.agregar_tarea("Tarea 1")
    assert len(gestor.tareas) == 1

def test_eliminar_tarea(gestor):
    gestor.agregar_tarea("Tarea 1")
    tarea_eliminada = gestor.eliminar_tarea(1)
    assert tarea_eliminada == "Tarea 1"
    assert len(gestor.tareas) == 0

def test_obtener_tarea(gestor):
    gestor.agregar_tarea("Tarea 1")
    tarea_obtenida = gestor.obtener_tarea(1)
    assert tarea_obtenida == "Tarea 1"

def test_actualizar_tarea(gestor):
    gestor.agregar_tarea("Tarea 1")
    gestor.actualizar_tarea(1, "Tarea 2")
    tarea_actualizada = gestor.obtener_tarea(1)
    assert tarea_actualizada == "Tarea 2"

if __name__ == "__main__":
    pytest.main()
