import json


def generar_json(direccion_archivo, datos):
    """
    Genera un archivo JSON con los datos proporcionados.

    Args:
        direccion_archivo (str): La ruta donde se guardará el archivo JSON.
        datos (dict): Los datos que se escribirán en el archivo JSON.

    Raises:
        Exception: Si ocurre un error durante la escritura del archivo.
    """
    try:
        with open(direccion_archivo, 'w') as archivo_json:
            json.dump(datos, archivo_json, indent=4)
        print("El archivo se ha generado con exito.")
    except Exception as e:
        print(f"Ocurrio un error: {e}")

# Ejemplo de uso de la función generar_json

datos = {
    "nombre": "Andres Felipe",
    "edad": 33,
    "profesion": "Ingeniero",
    "habilidades": ["Python", "Java", "SCRUM", "Redes"],
    "proyecto": [
        {"nombre": "Procesamiento de datos", "Universidad": "UTP"},
        {"nombre": "Articulo Q1", "Universidad": "CIAF"}
    ]
}

direccion = r"C:\Users\pipe_\OneDrive\Desktop\docente.json"
generar_json(direccion, datos)
