from product import Producto, Electronico, Ropa, Alimento
from product_handler import GestorPedidos
from file_manager import GestorArchivos


def main():
    gestor_pedidos = GestorPedidos()
    gestor_archivos = GestorArchivos("productos.json")

    # Load existing data
    gestor_pedidos.productos = gestor_archivos.cargar_archivo()

    # Initialize products if no data is loaded
    if not gestor_pedidos.productos:
        gestor_pedidos.agregar_producto(Electronico('Laptop', 1200, 10, 2))
        gestor_pedidos.agregar_producto(Ropa('Camiseta', 20, 50, 'M'))
        gestor_pedidos.agregar_producto(Alimento('Pizza Congelada', 8, 100, '2024-12-01'))

    continuar = True

    while continuar:
        try:
            opcion = int(input('''
            ----------------
            Menu principal:
            1. Mostrar los productos disponibles.
            2. Realizar un pedido.
            3. Guardar productos en archivo.
            4. Salir
            Digite una opcion: '''))

            if opcion == 1:
                gestor_pedidos.mostrar_productos_disponibles()
            elif opcion == 2:
                nombre_producto = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio_total = gestor_pedidos.realizar_pedido(nombre_producto, cantidad)
                precio_total = GestorPedidos.aplicar_descuento(precio_total, cantidad)
                print(f"Total a pagar: {precio_total}")
            elif opcion == 3:
                gestor_archivos.guardar_archivo(gestor_pedidos.productos)
            elif opcion == 4:
                continuar = False
            else:
                print("Opción no válida.")
        except ValueError:
            print("Entrada inválida, por favor ingrese un número válido.")


if __name__ == "__main__":
    main()
