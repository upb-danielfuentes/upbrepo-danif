# Realice un algoritmo que permita validar si la pwd ingresada es correcta,

def pwd():
    pwd = "1234"
    pwdIngresada = input("Ingrese su contraseña: ")
    while pwdIngresada != pwd:
        pwdIngresada = input("Ingrese su contraseña: ")
    print("🔓 Contraseña correcta")
pwd() 