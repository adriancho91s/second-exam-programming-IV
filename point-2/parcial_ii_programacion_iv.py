# Clase base
class Habitacion:
    def __init__(self, numero, precio, estado="Disponible"):
        self.__numero = numero
        self.__precio = precio
        self.__estado = estado

    def obtener_numero(self):
        return self.__numero

    def obtener_precio(self):
        return self.__precio

    def obtener_estado(self):
        return self.__estado

    def cambiar_estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def nombrar_habitacion(self):
        raise NotImplementedError("Este método debe ser implementado en la subclase.")

# Clase HabitacionSimple
class HabitacionSimple(Habitacion):
    def nombrar_habitacion(self):
        return "Habitacion Simple"

# Clase HabitacionDoble
class HabitacionDoble(Habitacion):
    def __init__(self, numero, precio, estado="Disponible"):
        super().__init__(numero, precio, estado)
        self.servicios = []

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def calcular_precio_total(self):
        return self.obtener_precio() + sum(servicio['precio'] for servicio in self.servicios)

    def nombrar_habitacion(self):
        return "Habitacion Doble"

# Clase Suite
class Suite(Habitacion):
    def __init__(self, numero, precio, estado="Disponible"):
        super().__init__(numero, precio, estado)
        self.servicios = []

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def calcular_precio_total(self):
        return self.obtener_precio() + sum(servicio['precio'] for servicio in self.servicios)

    def nombrar_habitacion(self):
        return "Suite"

# Función para mostrar habitaciones disponibles
def mostrar_habitaciones_disponibles(habitaciones):
    print("\nHabitaciones disponibles:")
    disponibles = False
    for habitacion in habitaciones.values():
        if habitacion.obtener_estado() == "Disponible":
            print(f"Habitación {habitacion.obtener_numero()}: {habitacion.nombrar_habitacion()}, Precio: {habitacion.obtener_precio()}")
            disponibles = True
    if not disponibles:
        print("No hay habitaciones disponibles.")

# Función para reservar una habitación
def reservar_habitacion(habitaciones, numero_habitacion):
    if numero_habitacion in habitaciones:
        habitacion = habitaciones[numero_habitacion]
        if habitacion.obtener_estado() == "Disponible":
            habitacion.cambiar_estado("Reservada")
            print(f"Habitación {numero_habitacion} reservada exitosamente.")
        else:
            print(f"La habitación {numero_habitacion} ya está reservada.")
    else:
        print(f"La habitación {numero_habitacion} no existe.")

# Función para calcular el precio total de una habitación con servicios adicionales
def calcular_precio_total(habitaciones, numero_habitacion):
    if numero_habitacion in habitaciones:
        habitacion = habitaciones[numero_habitacion]
        if isinstance(habitacion, (HabitacionDoble, Suite)):
            print(f"Precio total de la habitación {numero_habitacion} con servicios adicionales: {habitacion.calcular_precio_total()}")
        else:
            print(f"La habitación {numero_habitacion} es una {habitacion.nombrar_habitacion()} y no tiene servicios adicionales.")
    else:
        print(f"La habitación {numero_habitacion} no existe.")


def mostrar_numeros_habitaciones_disponibles(habitaciones):
  print("\nHabitaciones Disponibles:")
  disponibles = False
  for habitacion in habitaciones.values():
    if habitacion.obtener_estado() == "Disponible":
      disponibles = True
      print(f"{habitacion.obtener_numero()} - ", end="")
  if not disponibles:
    print("No hay habitaciones disponibles\n")

# Función para inicializar las habitaciones en el sistema
def inicializar_habitaciones():
    habitaciones = {
        101: HabitacionSimple(101, 100),
        102: HabitacionDoble(102, 200),
        103: Suite(103, 300),
        104: HabitacionSimple(104, 100),
        105: HabitacionDoble(105, 200, "Reservada"),
        106: Suite(106, 300)
    }
    # Agregar algunos servicios a las habitaciones dobles y suites
    habitaciones[102].agregar_servicio({'nombre': 'Desayuno', 'precio': 20})
    habitaciones[106].agregar_servicio({'nombre': 'Spa', 'precio': 50})
    return habitaciones


# Función principal
def main():
    habitaciones = inicializar_habitaciones()
    continuar = True

    while continuar:
        try:
            opcion = int(input('''
    1. Mostrar habitaciones disponibles.
    2. Reservar una habitacion.
    3. Mostrar precio total con servicios incluidos.
    4. Salir.
    Digite una opcion: '''))

            match(opcion):
                case 1:
                    mostrar_habitaciones_disponibles(habitaciones)
                case 2:
                    mostrar_numeros_habitaciones_disponibles(habitaciones)
                    numero_habitacion = int(input("\nIngrese el número de la habitación que desea reservar: "))
                    reservar_habitacion(habitaciones, numero_habitacion)
                case 3:
                    numero_habitacion = int(input("Ingrese el número de la habitación para ver el precio total: "))
                    calcular_precio_total(habitaciones, numero_habitacion)
                case 4:
                    continuar = False
                    print("Gracias por usar el sistema de reservas. ¡Hasta luego!")
                case _:
                    print("Opción ingresada inválida, por favor digite una opción válida.\n")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Llamada a la función principal
if __name__ == "__main__":
    main()