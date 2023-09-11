from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

# Conecta a MongoDB (asegúrate de que MongoDB esté ejecutándose en el puerto predeterminado 27017)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mi_db"]
estudiantes = db["estudiantes"]

# Ruta para crear un estudiante (POST)
@app.route('/estudiantes', methods=['POST'])
def crear_estudiante():
    data = request.json
    nombre = data.get('nombre')
    edad = data.get('edad')
    estudiante = {"nombre": nombre, "edad": edad}
    estudiantes.insert_one(estudiante)
    return jsonify({"message": f"Estudiante {nombre} creado con éxito."})

# Ruta para obtener todos los estudiantes (GET)
@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    estudiantes_list = list(estudiantes.find())
    return jsonify(estudiantes_list)

# Ruta para obtener un estudiante por nombre (GET)
@app.route('/estudiantes/<string:nombre>', methods=['GET'])
def obtener_estudiante_por_nombre(nombre):
    estudiante = estudiantes.find_one({"nombre": nombre})
    if estudiante:
        return jsonify(estudiante)
    else:
        return jsonify({"message": f"No se encontró ningún estudiante con el nombre {nombre}."}), 404

# Ruta para actualizar la edad de un estudiante por nombre (PUT)
@app.route('/estudiantes/<string:nombre>', methods=['PUT'])
def actualizar_edad(nombre):
    data = request.json
    nueva_edad = data.get('edad')
    estudiantes.update_one({"nombre": nombre}, {"$set": {"edad": nueva_edad}})
    return jsonify({"message": f"Edad del estudiante {nombre} actualizada con éxito."})

# Ruta para eliminar un estudiante por nombre (DELETE)
@app.route('/estudiantes/<string:nombre>', methods=['DELETE'])
def eliminar_estudiante(nombre):
    estudiantes.delete_one({"nombre": nombre})
    return jsonify({"message": f"Estudiante {nombre} eliminado con éxito."})

if __name__ == '__main__':
    app.run(debug=True)
