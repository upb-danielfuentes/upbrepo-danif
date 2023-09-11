import pytest
from connection import ConexionMySQL, InsertarEstudiante, ActualizarEstudiante, EliminarEstudiante, ConsultarEstudiantes

# Prueba unitaria para la clase ConexionMySQL
def test_conexion_mysql():
    conexion = ConexionMySQL('root', '', 'localhost', 'upb')
    conexion.conectar()
    assert conexion.conexion.is_connected()
    conexion.cerrar()
    assert not conexion.conexion.is_connected()

# Prueba unitaria para la clase InsertarEstudiante
def test_insertar_estudiante():
    conexion = ConexionMySQL('root', '', 'localhost', 'upb')
    conexion.conectar()
    insertar = InsertarEstudiante(conexion.conexion)
    insertar.ejecutar(1, 'Estudiante1', 20)

    # Verificar si el estudiante se insertó correctamente
    consultar = ConsultarEstudiantes(conexion.conexion)
    registros = consultar.ejecutar()
    assert (1, 'Estudiante1', 20) in registros

    conexion.cerrar()

# Prueba unitaria para la clase ActualizarEstudiante
def test_actualizar_estudiante():
    conexion = ConexionMySQL('tu_usuario', 'tu_contraseña', 'localhost', 'upb')
    conexion.conectar()
    actualizar = ActualizarEstudiante(conexion.conexion)
    actualizar.ejecutar(1, 'EstudianteActualizado', 25)

    # Verificar si la actualización se realizó correctamente
    consultar = ConsultarEstudiantes(conexion.conexion)
    registros = consultar.ejecutar()
    assert (1, 'EstudianteActualizado', 25) in registros

    conexion.cerrar()

# Prueba unitaria para la clase EliminarEstudiante
def test_eliminar_estudiante():
    conexion = ConexionMySQL('tu_usuario', 'tu_contraseña', 'localhost', 'upb')
    conexion.conectar()
    eliminar = EliminarEstudiante(conexion.conexion)
    eliminar.ejecutar(1)

    # Verificar si el estudiante se eliminó correctamente
    consultar = ConsultarEstudiantes(conexion.conexion)
    registros = consultar.ejecutar()
    assert (1, 'EstudianteActualizado', 25) not in registros

    conexion.cerrar()

if __name__ == "__main__":
    pytest.main()
