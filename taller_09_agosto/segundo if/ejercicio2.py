# Escribir las estructuras Itogicas que calculen y muestren el valor de X de acuerdo con las siguientes condiciones:
# X=1 si Y>z
# X=2 si Y<=Z
# El usuario me debe ingresar el valor de Y y el valor de Z

X = 0
Y = int(input("Ingrese el valor de Y: "))
Z = int(input("Ingrese el valor de Z: "))

if Y > Z:
    X = 1
    print("X = ", X)
else:
    if Y <= Z:
        X = 2
        print("X = ", X)

print("Fin del programa")
