import os
import json

def ver_estado_proceso_camper(ruta_archivo):
    camper_id = input("Ingrese el ID del camper: ")

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)

        if camper_id in campus['campers']:
            estado = campus['campers'][camper_id].get('estado', 'Estado no disponible')
            print(f"\u001b[38;5;10mEstado actual del proceso\u001b[0m: {estado}")
        else:
            print("\u001b[38;5;196mID de camper no encontrado.\u001b[0m")
    else:
        print("Archivo campus.json no encontrado.")