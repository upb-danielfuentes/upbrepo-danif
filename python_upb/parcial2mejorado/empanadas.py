class EmpanadaShop:
    def __init__(self):
        self.menu_empanadas = {
            "Carne": 2.5,
            "Pollo": 2.0,
            "Queso": 1.8,
            "Papa": 2.2
        }

    def run(self):
        try:
            print("🚀 Iniciando programa 🚀")
            input("Bienvenido a la empanadita don Morcillin, presione Enter para continuar...")
            num_empanadas = self.get_valid_int_input("Ingrese el número de pedidos 🌮 a comprar: ")
            total_costo = self.calculate_total_cost(num_empanadas)

            print(f"\n 💸 Costo total de la compra de empanaditas don Morcillin es de: ${total_costo:.2f} 💸")
            self.show_payment_options()
            print("🚀 Finalizando programa 🚀")

        except ValueError:
            print("🚫 Cantidad de empanadas no válida. Debe ser un número entero. 🚫")
        except KeyboardInterrupt:
            print("\n 🚫 Proceso interrumpido por el usuario.🚫")

    def get_valid_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("🚫 Valor no válido. Debe ser un número entero. 🚫")

    def calculate_total_cost(self, num_empanadas):
        total_cost = 0
        for i in range(num_empanadas):
            print(f"Pedido 🌮 {i + 1}:")
            print("Tipos de empanadas disponibles (🥩, 🍗, 🧀, 🥔):")
            for tipo in self.menu_empanadas:
                print(f"- {tipo}")
            tipo_empanada = self.get_valid_empanada_type()
            cantidad = self.get_valid_int_input(f"Cuantas empandas de {tipo_empanada} quieres comprar: ")
            costo_empanada = self.menu_empanadas[tipo_empanada]
            costo_total_empanada = cantidad * costo_empanada
            total_cost += costo_total_empanada
            print(f"💵 El Costo de {cantidad} empanadas de {tipo_empanada}: ${costo_total_empanada:.2f} 💵")
            print("--------------------------------------------------")
        return total_cost

    def get_valid_empanada_type(self):
        while True:
            tipo_empanada = input("Que tipo de empanada deseas?: ")
            if tipo_empanada in self.menu_empanadas:
                return tipo_empanada
            else:
                print("🚫 Tipo de empanada no válido. 🚫")

    def show_payment_options(self):
        medios_validos = ["Nequi", "Bancolombia", "Efectivo", "Tarjeta"]
        try:
            mediopago = input("Escriba su medio de pago: ")
            if mediopago in medios_validos:
                self.display_payment_info(mediopago)
            else:
                print("Medio de pago no válido")
        except KeyboardInterrupt:
            print("\n 🚫 Proceso interrumpido por el usuario.🚫")

    def display_payment_info(self, mediopago):
        payment_info = {
            "Nequi": "Consigne a este número: 3013366588",
            "Bancolombia": "Número de cuenta: 1993823",
            "Efectivo": "Puede pagar en efectivo al momento de la entrega",
            "Tarjeta": "Puede pagar con tarjeta al momento de la entrega"
        }
        print(payment_info[mediopago])


if __name__ == "__main__":
    shop = EmpanadaShop()
    shop.run()
