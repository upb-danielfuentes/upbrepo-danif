import conexion as con 

def agregarEmpleado(persona):
    persona = dict(persona)

    try:
        db = con.conectar()
        miCursor = db.cursor()

        columnas = tuple(persona.keys())
        valores = tuple(persona.values())
    
        sql = "INSERT INTO tbl_Empleados {campos} VALUES(?,?,?,?,?,?)".format(campos=columnas)
        miCursor.execute(sql,valores)
        creada = miCursor.rowcount > 0
        db.commit()
        if creada:
            db.close()
            return{"Respuesta":True, "Mensaje":"Empleado resgistrado en la base de datos"}
        else: 
            db.close()
            return{"Respuesta":False, "Mensaje":"El empleado no fue agregado a la base de datos"}
        
    except Exception as ex: 
        db.close()
        return{"Respuesta":False, "Mensaje":str(ex)}
    
def listaTodosDatos():

     try:
         db = con.conectar()
         miCursor = db.cursor()
    
         sql = "SELECT * FROM tbl_Empleados ORDER BY apellido_empleado"
         miCursor.execute(sql)
         empleado = miCursor.fetchall()
         db.commit()
         if empleado:
            miCursor.close()
            db.close()
            return{"Respuesta":True, "Mensaje":empleado}
         else: 
            miCursor.close
            db.close()
            return{"Respuesta":False, "Mensaje":"El empleado no fue agregado a la base de datos"}
         
     except Exception as ex: 
        miCursor.close()
        db.close()
        return{"Respuesta":False, "Mensaje":str(ex)}
        
def listaEmpleado(ID_Empleado):

     try:
         db = con.conectar()
         miCursor = db.cursor()
    
         sql = "SELECT * FROM tbl_Empleados where id_empleado = "+ ID_Empleado
         miCursor.execute(sql)
         empleado = miCursor.fetchall()
         db.commit()
         
         if empleado:
            info = empleado[0]
            DatoBusqueda = {
                "id_empleado":info[0],
                "doc_empleado":info[1],
                "nombre_empleado":info[2],
                "apellido_empleado":info[3],
                "edad_empleado":info[4],
                "correo_empleado":info[5],
                "direccion_empleado":info[6]
            }
            miCursor.close()
            db.close()
            return{"Respuesta":True, "Mensaje":DatoBusqueda}
         else: 
            miCursor.close
            db.close()
            return{"Respuesta":False, "Mensaje":"El empleado no fue agregado a la base de datos"}
         
     except Exception as ex: 
        miCursor.close()
        db.close()
        return{"Respuesta":False, "Mensaje":str(ex)}
    
def actualizarEmpleado(empleado):
    empleado = dict(empleado)
    try:
         db = con.conectar()
         miCursor = db.cursor()

         valores = tuple(empleado.values())
         doc_empleado = empleado.get("doc_empleado")
         sql = """UPDATE tbl_Empleados SET doc_Empleado=?,nombre_empleado=?, 
                apellido_empleado=?,edad_empleado=?,correo_empleado=?,
                direccion_empleado=? WHERE doc_empleado = {DOC_EMPLE}""".format(DOC_EMPLE=doc_empleado)
         miCursor.execute(sql, valores)
         modificado = miCursor.rowcount>0
         db.commit()
         
         if modificado:
            miCursor.close()
            db.close()
            return{"Respuesta":True, "Mensaje":"Empleado Actualizado"}
         else: 
            miCursor.close
            db.close()
            return{"Respuesta":False, "Mensaje":"El empleado no fue agregado a la base de datos"}
    except Exception as ex: 
        miCursor.close()
        db.close()
        return{"Respuesta":False, "Mensaje":str(ex)}

def eliminarEmpleado(id):

     try:
         db = con.conectar()
         miCursor = db.cursor()

         sql = """DELETE FROM tbl_Empleados 
                  WHERE id_empleado={ID_EMPLE}""".format(ID_EMPLE=id)
         miCursor.execute(sql)
         db.commit()

         eliminado = miCursor.rowcount>0
         
         if eliminado:
            miCursor.close()
            db.close()
            return{"Respuesta":True, "Mensaje": "Eliminado el Empleado"}
         else: 
            miCursor.close
            db.close()
            return{"Respuesta":False, "Mensaje":"El empleado no fue Eliminado de la base de datos"}
         
     except Exception as ex: 
        miCursor.close()
        db.close()
        return{"Respuesta":False, "Mensaje":str(ex)}

