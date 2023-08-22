# Veterinaria UPB 🐾
# Programa que permite a los usuarios obtener recomendaciones para el cuidado de sus mascotas 🐶🐱🐰
# según la especie y la edad de la mascota. 📋🐾

def veterinaria():
    # Definir recomendaciones según la especie y la edad 📝📆
    recomendaciones = {
        "Perro": {
            "Cachorro": "Vacunación, desparasitación y socialización. 🐾🩺🏞️",
            "Adulto": "Control de salud anual, ejercicio regular y alimentación balanceada. 🏥🏃🍖",
            "Anciano": "Exámenes geriátricos, dieta especial y cuidado de articulaciones. 👴🔬💊"
        },
        "Gato": {
            "Cachorro": "Vacunación, desparasitación y cuidado de la caja de arena. 🐾🩺🗑️",
            "Adulto": "Control de salud anual, enriquecimiento ambiental y alimentación adecuada. 🏥🌿🍗",
            "Anciano": "Exámenes geriátricos, dieta para la salud renal y atención a problemas dentales. 👴🔬🦷"
        },
        "Conejo": {
            "Cachorro": "Vacunación, jaula segura y dieta equilibrada. 🐾🩺🏠",
            "Adulto": "Control de salud regular, espacio para ejercitarse y heno fresco. 🏥🏋️🌾",
            "Anciano": "Cuidado de dientes desgastados, dieta rica en fibra y chequeos frecuentes. 👴🦷🥦"
        }
    }

    try:
        cantidad_mascotas = int(input("Ingrese la cantidad de mascotas que tiene: "))
        for i in range(cantidad_mascotas):
            nombre_mascota = input(f"Ingrese el nombre de su mascota #{i+1}: ")
            especie = input(f"Ingrese la especie de {nombre_mascota} (Perro, Gato, Conejo, etc.): ")
            edad = int(input(f"Ingrese la edad de {nombre_mascota} en años: "))

            if especie in recomendaciones:
                print("\nRecomendaciones para su mascota:")
                if edad < 1:
                    etapa = "Cachorro"
                elif edad <= 7:
                    etapa = "Adulto"
                else:
                    etapa = "Anciano"

                print(f"Nombre de la mascota: {nombre_mascota}")
                print(f"Especie: {especie}")
                print(f"Edad: {edad} años")
                print(f"Etapa de vida: {etapa}")

                if etapa in recomendaciones[especie]:
                    print(f"Recomendaciones: {recomendaciones[especie][etapa]}")
                else:
                    print("No se encontraron recomendaciones para esta etapa. 😕")
            else:
                print("Especie no válida. Por favor, ingrese una especie válida. 🚫🦉")
    except ValueError:
        print("Edad no válida. Debe ser un número entero. ❌🔢")
    except Exception as e:
        print("Ocurrió un error:", e)

veterinaria()
