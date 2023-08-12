# En un juego de preguntas que se responde "SI" o "No" gana quien responda correctamente las 3 preguntas.
# Si se responde mal cualquiera de ellas , ya no se pregunta la siguiente y termina el juego
# Simo Bolivar libero a colombia?
# Dario gomez fue el rey de despecho?
# El binomio de oro es un grupo musica vallenata?

def juego_preguntas():
    print("Bienvenido al juego de preguntas. Responde 'SI' o 'No'.")
    
    respuesta_1 = input("¿Simón Bolívar liberó a Colombia? ")
    if respuesta_1 == "SI" or respuesta_1 == "si":
        respuesta_2 = input("¿Dario Gómez fue el rey del despecho? ")
        if respuesta_2 == "SI" or respuesta_2 == "si":
            respuesta_3 = input("¿El Binomio de Oro es un grupo musical vallenato? ")
            if respuesta_3 == "SI" or respuesta_3 == "si":
                print("¡Felicidades! ¡Has respondido correctamente a todas las preguntas!")
            else:
                print("Respuesta incorrecta. Fin del juego.")
        else:
            print("Respuesta incorrecta. Fin del juego.")
    else:
        print("Respuesta incorrecta. Fin del juego.")

juego_preguntas()
