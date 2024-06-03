import os
import json

def ver_estado_proceso(ruta_archivo):
    camper_id = input("Ingrese su ID de camper: ")

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)

        if camper_id in campus['campers']:
            estado = campus['campers'][camper_id].get('estado', 'Estado no disponible')
            print(f"Estado actual del proceso: {estado}")
        else:
            print("ID de camper no encontrado.")
    else:
        print("Archivo campus.json no encontrado.")