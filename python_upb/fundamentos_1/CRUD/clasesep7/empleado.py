import connection as con

def AgregarEmpleado (persona):
    persona = dict(persona)
    try:
        db = con.conectar()
        miCursor = db.cursor()
        columnas = tuple(persona.keys()) # keys() devuelve una lista de las llaves del diccionario
        valores = tuple(persona.values()) # values() devuelve una lista de los valores del diccionario
        sql = "insert into tbl_Empleados {campos} values(?,?,?,?,?,?)".format(campos=columnas) #format() reemplaza los {} por los valores de las variables
        miCursor.execute(sql, valores)
        creada = miCursor.rowcount>0
        db.commit()
        if creada:
            db.close()
            return {'Respuesta':True , 'Mensaje':'Empleado agregado con éxito 😊'}
        else:
            db.close()
            return {'Respuesta':False , 'Mensaje':'No se pudo agregar el empleado 😭'}
    except Exception as ex:
        db.close()
        return {'Respuesta':False , 'Mensaje':str(ex)}
    finally:
        db.close() 