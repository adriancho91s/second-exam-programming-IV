import json
from product import Producto, Electronico, Ropa, Alimento

class GestorArchivos:
    def __init__(self, filename):
        self.filename = filename

    def guardar_archivo(self, productos):
        try:
            with open(self.filename, 'w') as file:
                json.dump([self.producto_a_dict(p) for p in productos.values()], file, indent=4)
                print("Datos guardados con éxito.")
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def cargar_archivo(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                if not data:
                    return {}
                return {d['nombre']: self.dict_a_producto(d) for d in data}
        except FileNotFoundError:
            print(f"Archivo {self.filename} no encontrado. Se creará uno nuevo.")
            with open(self.filename, 'w') as file:
                file.write("[]")
            return []
        except json.JSONDecodeError:
            print(f"Archivo {self.filename} está vacío o corrupto. Se creará uno nuevo.")
            with open(self.filename, 'w') as file:
                file.write("[]")
            return []
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            return {}

    @staticmethod
    def producto_a_dict(producto):
        data = {
            "nombre": producto.nombre,
            "precio": producto.precio,
            "cantidad": producto.cantidad,
            "tipo": type(producto).__name__,
        }
        if isinstance(producto, Electronico):
            data["periodo_de_garantia"] = producto._periodo_de_garantia
        elif isinstance(producto, Ropa):
            data["tamanio"] = producto._tamanio
        elif isinstance(producto, Alimento):
            data["fecha_de_caducidad"] = producto._fecha_de_caducidad
        return data

    @staticmethod
    def dict_a_producto(data):
        tipo = data["tipo"]
        if tipo == "Electronico":
            return Electronico(data["nombre"], data["precio"], data["cantidad"], data["periodo_de_garantia"])
        elif tipo == "Ropa":
            return Ropa(data["nombre"], data["precio"], data["cantidad"], data["tamanio"])
        elif tipo == "Alimento":
            return Alimento(data["nombre"], data["precio"], data["cantidad"], data["fecha_de_caducidad"])
