import json
import os

def ver_informacion_camper(ruta_archivo):
    camper_id = input("Ingrese su ID de camper: ")
    
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)
            
        if camper_id in campus['campers']:
            print("\u001b[38;5;10mInformación del Camper:\u001b[0m")
            for key, value in campus['campers'][camper_id].items():
                print(f"{key}: {value}")
        else:
            print("\u001b[38;5;196mID de camper no encontrado.\u001b[0m")
    else:
        print("Archivo campus.json no encontrado.")