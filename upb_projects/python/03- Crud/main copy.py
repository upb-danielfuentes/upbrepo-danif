import empleado as emp

regEmpleado = {"doc_empleado":"158545",
                "nombre_empleado":"AA",
                "apellido_empleado":"PeDDrez",
                "edad_empleado":819,
                "correo_empleado":"chucha@gmail.com",
                "direccion_empleado":"perrolandia Falsa 123"}

Respuestauno = emp.agregarEmpleado(regEmpleado)

respuestados = emp.listaTodosDatos()

respuestaselecta = emp.listaEmpleado("5")

respuestaactualizada = emp.actualizarEmpleado(regEmpleado)

respuestaborrado = emp.eliminarEmpleado("12")

print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")
print ("---------------- Respuesta Empleado Creado -------------")
print(Respuestauno)
print ("---------------- Respuesta Empleado Creado -------------")
print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")

print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")
print ("---------------- Respuesta toda Inicio -------------")
print(respuestados)
print ("---------------- Respuesta toda Fin -------------")
print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")

print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")
print ("---------------- Respuesta Selecta Inicio -------------")
print(respuestaselecta)
print ("---------------- Respuesta Selecta Fin -------------")
print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")

print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")
print ("---------------- Respuesta Actualizacion Inicio -------------")
print(respuestaactualizada)
print ("---------------- Respuesta Actualizacion Fin -------------")
print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")

print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")
print ("---------------- Respuesta Eliminado Inicio -------------")
print(respuestaborrado)
print ("---------------- Respuesta Eliminado Fin -------------")
print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")

print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")
print ("---------------- Respuesta toda Inicio -------------")
print(respuestados)
print ("---------------- Respuesta toda Fin -------------")
print ("-*/-*/-/-*/-/-/-/-*/-*/-*/-/-*/-*/-*/-*/-*/-*/-*/-")