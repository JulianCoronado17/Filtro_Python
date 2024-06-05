import os
import json

def asignar_area_a_trainer(ruta_archivo):
    trainer_id = input("Ingrese el ID del trainer: ")
    nueva_area = input("Ingrese la nueva área del trainer: ")

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)

        if trainer_id in campus['trainers']:
            campus['trainers'][trainer_id]['area'] = nueva_area
            with open(ruta_archivo, 'w') as archivo_json:
                json.dump(campus, archivo_json, indent=4)
            print("\u001b[38;5;10mÁrea asignada exitosamente.\u001b[0m")
        else:
            print("\u001b[38;5;196mID de trainer no encontrado.\u001b[0m")
    else:
        print("Archivo campus.json no encontrado.")