class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    def reducir_cantidad(self, cantidad):
        if cantidad <= self._cantidad:
            self._cantidad -= cantidad
        else:
            print("No hay suficiente stock disponible.")

    def mostrar_detalles(self):
        return f"{self._nombre} - Precio: {self._precio} - Cantidad disponible: {self._cantidad}"


class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad, periodo_de_garantia):
        super().__init__(nombre, precio, cantidad)
        self._periodo_de_garantia = periodo_de_garantia

    def mostrar_detalles(self):
        return f"{self._nombre} (Electrónico) - Precio: {self._precio} - Garantía: {self._periodo_de_garantia} años - Cantidad: {self._cantidad}"


class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, tamanio):
        super().__init__(nombre, precio, cantidad)
        self._tamanio = tamanio

    def mostrar_detalles(self):
        return f"{self._nombre} (Ropa) - Precio: {self._precio} - Tamaño: {self._tamanio} - Cantidad: {self._cantidad}"


class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_de_caducidad):
        super().__init__(nombre, precio, cantidad)
        self._fecha_de_caducidad = fecha_de_caducidad

    def mostrar_detalles(self):
        return f"{self._nombre} (Alimento) - Precio: {self._precio} - Caducidad: {self._fecha_de_caducidad} - Cantidad: {self._cantidad}"
