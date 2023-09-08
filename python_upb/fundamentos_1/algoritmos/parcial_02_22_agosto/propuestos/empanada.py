def empanadas():
    menu_empanadas = {
        "Carne": 2.5,
        "Pollo": 2.0,
        "Queso": 1.8,
        "Papa": 2.2
    }
    try:
        print("🚀 Iniciando programa 🚀")
        input("Bienvenidos a Don Morcillin, presione Enter para continuar...")
        num_pedidos = int(input("Ingrese el número de pedidos 🌮 a comprar: "))
        total_costo = 0

        for i in range(num_pedidos):
            print(f"Este es el Pedido 🌮 {i + 1}:")
            print("Tipos de empanadas disponibles (🥩, 🍗, 🧀, 🥔):")
            for tipo in menu_empanadas:
                print(f"- {tipo}")

            tipo_empanada = input("Que tipo de empanada deseas?: ")
            if tipo_empanada in menu_empanadas:
                try:
                    cantidad = int(input(f"Cuantas empanadas de {tipo_empanada} quiere sumerce: "))
                    costo_empanada = menu_empanadas[tipo_empanada]
                    costo_total_empanada = cantidad * costo_empanada
                    total_costo += costo_total_empanada
                    print(f"💵 El Costo de {cantidad} empanadas de {tipo_empanada}: ${costo_total_empanada:.2f} 💵") # .2f: Indica formatear el número con 2 decimales después del punto decimal.
                    print("--------------------------------------------------")
                except ValueError:
                    print("🚫 Cantidad no válida. Debe ser un número entero. 🚫")
            else:
                print("🚫 Tipo de empanada no válido. 🚫")
        
        print(f"\n 💸 Costo total de la compra de empanaditas don Morcillin es de: ${total_costo:.2f} 💸")
        medioPago()  # Llamar a medioPago aquí para mostrar opciones de pago
        print("🚀 Finalizando programa 🚀")
    
    except ValueError:
        print("🚫 Cantidad de empanadas no válida. Debe ser un número entero. 🚫")
    except KeyboardInterrupt:
        print("\n 🚫 Proceso interrumpido por el usuario.🚫")

def medioPago():
    try:  
        medios_validos = ["Nequi", "Bancolombia", "Efectivo", "Tarjeta"]
        mediopago = input("Cual va a ser su medio de pago? (Nequi, Bancolombia, Efectivo, Tarjeta: ")
        if mediopago in medios_validos:
            if mediopago == "Nequi":
                print("Consigne a este número: 3013366588")
            elif mediopago == "Bancolombia":
                print("Número de cuenta: 1993823")
            elif mediopago == "Efectivo":
                print("Puede pagar en efectivo al momento de la entrega")
            elif mediopago == "Tarjeta":
                print("Puede pagar con tarjeta al momento de la entrega")
        else:
            print("Medio de pago no válido")
    except KeyboardInterrupt:
        print("\n 🚫 Proceso interrumpido por el usuario.🚫")

empanadas()