import json

ARCHIVO_DATOS = "gastos.json"

def guardar_transacciones(lista):
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(lista, archivo, indent=4)
        print(f"> Datos respaldados con exito en {ARCHIVO_DATOS}.")
    except Exception as e:
        print(f"! Error al guardar archivo: {e}")

def cargar_transacciones():
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return[]
    except Exception as e:
        print(f"! error al cargar archivo: {e}")
        return[]
