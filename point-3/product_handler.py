class GestorPedidos:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.nombre] = producto

    def mostrar_productos_disponibles(self):
        print("\nProductos disponibles:")
        if self.productos:
            for producto in self.productos.values():
                print(producto.mostrar_detalles())
        else:
            print("No hay productos disponibles.")

    def realizar_pedido(self, nombre_producto, cantidad):
        if nombre_producto in self.productos:
            producto = self.productos[nombre_producto]
            if producto.cantidad >= cantidad:
                producto.reducir_cantidad(cantidad)
                print(f"Has pedido {cantidad} de {nombre_producto}.")
                return producto.precio * cantidad
            else:
                print("Cantidad insuficiente en stock.")
                return 0
        else:
            print("Producto no encontrado.")
            return 0

    @staticmethod
    def aplicar_descuento(precio_total, cantidad):
        if cantidad > 5:
            print("Se aplicará un descuento del 10% por la compra de más de 5 unidades.")
            return precio_total * 0.9  # 10% de descuento
        return precio_total
