# calculador_x.py

def calcular_x(y, z):
    if y > z:
        x = 1
        return x
    else:
        x = 2
        return x

if __name__ == "__main__":
    y = int(input("Ingrese el valor de Y: "))
    z = int(input("Ingrese el valor de Z: "))
    resultado = calcular_x(y, z)
    print("X =", resultado)
