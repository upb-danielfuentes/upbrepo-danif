print("🚀 Iniciando programa 🚀")
print("--------------------------------------------------")
# Solicitar al usuario la cantidad de números a analizar
n = int(input("Ingrese la cantidad de números a analizar: "))
print("--------------------------------------------------")

# Inicializar la lista para almacenar los números ingresados
numeros = []

# Solicitar al usuario que ingrese los n números uno por uno
for i in range(n):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Calcular la suma de los números ingresados
suma = 0
for numero in numeros:
    suma += numero

# Calcular la multiplicación de los números ingresados
multiplicacion = 1
for numero in numeros:
    multiplicacion *= numero

# Calcular el promedio de los números ingresados
promedio = suma / n

# Encontrar el número más grande y el número más pequeño
maximo = numeros[0]
minimo = numeros[0]
for numero in numeros:
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

# Encontrar números repetidos
numeros_repetidos = set() # Inicializar un conjunto vacío y lo almacena en la variable numeros_repetidos
numeros_no_repetidos = set() # Inicializar un conjunto vacío y lo almacena en la variable numeros_no_repetidos
for numero in numeros:
    if numero in numeros_no_repetidos:
        numeros_repetidos.add(numero) # .add() es un método que agrega un elemento a un conjunto
    else:
        numeros_no_repetidos.add(numero) # .add() es un método que agrega un elemento a un conjunto

# Mostrar los resultados
print("--------------------------------------------------")
print("Resultados:")
print("--------------------------------------------------")
print("➕ Suma:", suma)
print("✖️ Multiplicación:", multiplicacion)
print("➗ Promedio:", promedio)
print("🔺 Número más grande:", maximo)
print("🔻 Número más pequeño:", minimo)
print("🟰  Cantidad de números repetidos:", len(numeros_repetidos)) # len() es una función que devuelve la cantidad de elementos de un conjunto
print("--------------------------------------------------")
