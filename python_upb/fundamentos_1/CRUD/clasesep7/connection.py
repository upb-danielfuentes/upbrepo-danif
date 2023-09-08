import sqlite3
import sentry_sdk

def conectar():
    miConexion = sqlite3.connect('db_tienda_arepas.db')
    miCursor = miConexion.cursor()
    try:
        sql = """
        CREATE TABLE IF NOT EXISTS tbl_Empleados (
            id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_empleado VARCHAR(11) NOT NULL,
            nombre_empleado VARCHAR(50) NOT NULL,
            apellido_empleado VARCHAR(50) NOT NULL,
            edad_empleado INTEGER NOT NULL,
            correo_empleado VARCHAR(50) NOT NULL,
            direccion_empleado VARCHAR(50) NOT NULL    
        )
        """
        miCursor.execute(sql)
        miConexion.commit()
        print('Base de datos creada con éxito')
    except Exception as ex:
        sentry_sdk.capture_exception(ex)
        sentry_sdk.capture_message("Fallo la creacion de la DB")
    finally:
        miCursor.close()
        return miConexion
