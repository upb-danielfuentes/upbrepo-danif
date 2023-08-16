# Realice un algoritmo que me muestre los numero del 1 al 10

def mostrar_numeros_incremento():
    for i in range(1,11):
        print(i, end=", ")
    print ("")
mostrar_numeros_incremento()

def mostrar_numeros_incremento():
    for i in range(10,0,-1):
        print(i, end=" - ")
    print ("")
mostrar_numeros_incremento()

# Realice un algoritmo que capture la informacion de 5 personas
def cinco_personas():
    name = ""
    for i in range(1,6):
        print ("Persona", i)
        name = name + input("Ingrese su nombre: ") + " "
    print(name)
cinco_personas()



