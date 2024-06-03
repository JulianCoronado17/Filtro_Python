import os
import json

def actualizar_estado_riesgo_camper(ruta_archivo):
    camper_id = input("Ingrese el ID del camper: ")

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)

        if camper_id in campus['campers']:
            nuevo_estado = input("Ingrese el nuevo estado del camper: ")
            nuevo_riesgo = input("Ingrese el nuevo riesgo del camper: ")
            campus['campers'][camper_id]['estado'] = nuevo_estado
            campus['campers'][camper_id]['riesgo'] = nuevo_riesgo

            with open(ruta_archivo, 'w') as archivo_json:
                json.dump(campus, archivo_json, indent=4)
            print("Estado y riesgo actualizados exitosamente.")
        else:
            print("ID de camper no encontrado.")
    else:
        print("Archivo campus.json no encontrado.")