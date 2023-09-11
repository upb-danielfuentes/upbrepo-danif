import sqlite3

con = sqlite3.connect("dbempleadotest.db")
cursor = con.cursor()

# Funciones para la creación de tablas
cursor.execute("""
               CREATE TABLE IF NOT EXISTS tbl_Empleados (
                    id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
                    doc_empleado VARCHAR(11) NOT NULL,
                    nombre_empleado VARCHAR(50) NOT NULL,
                    apellido_empleado VARCHAR(50) NOT NULL,
                    edad_empleado INTEGER
               )
""")

# Funciones para la inserción de datos
sql = ("INSERT INTO tbl_Empleados VALUES (null,?,?,?,?)")
datos_insert = ('388383744', 'Maira', 'Yajari', 88)
cursor.execute(sql, datos_insert)
con.commit()

resultado_con = cursor.execute("SELECT * FROM tbl_Empleados")
print("///////////////////////////////")
print(resultado_con.fetchall())
print("///////////////////////////////")

res = cursor.execute("SELECT nombre_empleado,apellido_empleado FROM tbl_Empleados WHERE id_empleado = 9")
con.commit() # Guarda los cambios
print ("---------------------------------")
print (res.fetchone())
print ("---------------------------------")

update = cursor.execute("UPDATE tbl_Empleados SET nombre_empleado = 'Juan' WHERE id_empleado = 8")
con.commit() # Guarda los cambios
print ("---------------------------------")
print (update.fetchone()) # fetchone() trae el primer registro

delete = cursor.execute("DELETE FROM tbl_Empleados WHERE id_empleado = 7")
con.commit() #commit guarda los cambios
print ("---------------------------------")
print (delete.fetchone()) # fetchone() trae el primer registro



