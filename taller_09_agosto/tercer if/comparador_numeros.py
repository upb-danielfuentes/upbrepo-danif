# comparador_numeros.py

def comparar_numeros(a, b):
    if a > b:
        return "El primer numero es mayor que el segundo"
    elif a == b:
        return "El segundo numero es igual que el primero"
    else:
        return "El numero B es mayor"

if __name__ == "__main__":
    A = int(input("Ingrese el primer numero: "))
    B = int(input("Ingrese el segundo numero: "))
    resultado = comparar_numeros(A, B)
    print(resultado)
