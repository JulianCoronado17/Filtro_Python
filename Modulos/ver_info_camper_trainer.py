import os 
import json

def ver_info_camper_trainer(ruta_archivo):
    camper_id = input("Ingrese el ID del camper: ")

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)
        
        if camper_id in campus['campers']:
            print("Información del Camper:")
            for key, value in campus['campers'][camper_id].items():
                print(f"{key}: {value}")
        else:
            print("ID de camper no encontrado.")
    else:
        print("Archivo campus.json no encontrado.")