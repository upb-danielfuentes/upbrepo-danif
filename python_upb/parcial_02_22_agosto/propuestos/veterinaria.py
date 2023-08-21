# Definir recomendaciones según la especie y la edad
recomendaciones = {
    "Perro": {
        "Cachorro": "Vacunación, desparasitación y socialización.",
        "Adulto": "Control de salud anual, ejercicio regular y alimentación balanceada.",
        "Anciano": "Exámenes geriátricos, dieta especial y cuidado de articulaciones."
    },
    "Gato": {
        "Cachorro": "Vacunación, desparasitación y cuidado de la caja de arena.",
        "Adulto": "Control de salud anual, enriquecimiento ambiental y alimentación adecuada.",
        "Anciano": "Exámenes geriátricos, dieta para la salud renal y atención a problemas dentales."
    },
    "Conejo": {
        "Cachorro": "Vacunación, jaula segura y dieta equilibrada.",
        "Adulto": "Control de salud regular, espacio para ejercitarse y heno fresco.",
        "Anciano": "Cuidado de dientes desgastados, dieta rica en fibra y chequeos frecuentes."
    }
}

try:
    # Solicitar información al usuario sobre la mascotica
    nombre_mascota = input("Ingrese el nombre de su mascota: ")
    especie = input("Ingrese la especie de su mascota (Perro, Gato, Conejo, etc.): ")
    edad = int(input("Ingrese la edad de su mascota en años: "))

    # Validar la especie ingresada
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
            print("No se encontraron recomendaciones para esta etapa.")
    else:
        print("Especie no válida.")
except ValueError:
    print("Error: Ingrese un valor válido para la edad.")
except Exception as e:
    print("Ocurrió un error:", e)
