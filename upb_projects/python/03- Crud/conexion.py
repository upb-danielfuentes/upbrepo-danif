import sqlite3

def conectar():
    miConexion = sqlite3.connect("db_tienda_pedro.db")
    miCursor = miConexion.cursor()

    try: 
        sql = """
               CREATE TABLE IF NOT EXISTS tbl_Empleados (
                    id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
                    doc_empleado VARCHAR(11) NOT NULL,
                    nombre_empleado VARCHAR(50) NOT NULL,
                    apellido_empleado VARCHAR(50) NOT NULL,
                    edad_empleado INTEGER NOT NULL,
                    correo_empleado TEXT NOT NULL,
                    direccion_empleado TEXT
               )
"""
        miCursor.execute(sql)
        print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")
        print("Tabla y Base de datos creada con exito")
        print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")
        miCursor.close()
        return miConexion
    except Exception as ex:
        print("Error en la conexion: ", ex)
        miCursor.close()
    return miConexion