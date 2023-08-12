# Sabe en que rango de edad esta 

def rangoedad():
    nombre = input("Ingrese su nombre: ")
    genero = input("Ingrese su genero: ")
    year = int(input("Ingrese su fecha de nacimiento: " ))
    catMujer = "Mujer"
    catHombre = "Hombre"
    resultado1 = ""

    if genero == "F" or genero == "f":
        resultado1= catMujer
    else:
        if genero == "M" or genero == "m":
            resultado1=catHombre
        else:
            print("Ni M ni F categoria") 

    #Procesamiento de datos
    edad = 2023 - year
    catPersona = ""
    flag = False

    if edad > 0 and edad <= 106:
        if edad >0 and edad <=2:
            catPersona = "bebe"
            flag = True
        else:
            if edad >2 and edad <=10:
                catPersona = "nino"
                flag = True
            else:
                if edad >10 and edad <=17:
                    catPersona = "adole"
                    flag = True
                else:
                    if edad >17 and edad <=25:
                        catPersona = "joven"
                        flag = True
                    else:
                        if edad >25 and edad <=59:
                            catPersona = "adulto"
                            flag = True
                        else:
                            catPersona = "adulto mayor"
                            flag = True
    else:
        print("El numero ingresado no es valido")
        flag = False
    
    if flag and resultado1 != "":
        print("Hola ",nombre, "Su genero es:",resultado1, "la categoria suya es:",catPersona  )
    else:
        print("error")

rangoedad()