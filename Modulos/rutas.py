import os
import json

def ver_rutas_disponibles(ruta_archivo):
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)

        print("Rutas de entrenamiento disponibles:")
        for ruta in campus['rutas']:
            print(f"- {ruta.capitalize()}")
    else:
        print("Archivo campus.json no encontrado.")


def ver_todas_las_rutas(ruta_archivo):
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)
        
        print("Rutas disponibles:")
        for ruta in campus['rutas']:
            print(f"Ruta: {ruta}")
    else:
        print("Archivo campus.json no encontrado.")