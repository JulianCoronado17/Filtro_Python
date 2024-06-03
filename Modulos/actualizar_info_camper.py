import os
import json

def actualizar_informacion_camper(ruta_archivo):
    camper_id = input("Ingrese su ID de camper: ")

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)

        if camper_id in campus['campers']:
            print("Actualizar Información del Camper:")
            for key in campus['campers'][camper_id]:
                if key not in ["ID", "estado", "riesgo",'id']:
                    nuevo_valor = input(f"{key} actual ({campus['campers'][camper_id][key]}): ")
                    if nuevo_valor:
                        campus['campers'][camper_id][key] = nuevo_valor

            with open(ruta_archivo, 'w') as archivo_json:
                json.dump(campus, archivo_json, indent=4)
            print("Información actualizada.")
        else:
            print("ID de camper no encontrado.")
    else:
        print("Archivo campus.json no encontrado.")
