def obtener_rango_edad(year):
    if year > 2023 or year < 0:
        return None
    
    edad = 2023 - year

    if edad <= 2:
        return "bebe"
    elif edad <= 10:
        return "nino"
    elif edad <= 17:
        return "adole"
    elif edad <= 25:
        return "joven"
    elif edad <= 59:
        return "adulto"
    else:
        return "adulto mayor"

def obtener_genero(genero):
    genero = genero.lower()
    if genero == "f":
        return "Mujer"
    elif genero == "m":
        return "Hombre"
    else:
        return None

def main():
    nombre = input("Ingrese su nombre: ")
    genero = input("Ingrese su genero: ")
    year = int(input("Ingrese su fecha de nacimiento: " ))
    
    catPersona = obtener_rango_edad(year)
    catGenero = obtener_genero(genero)

    if catPersona is not None and catGenero is not None:
        print("Hola {}, su género es: {}, y su categoría es: {}".format(nombre, catGenero, catPersona))
    else:
        print("Error")

if __name__ == "__main__":
    main()
