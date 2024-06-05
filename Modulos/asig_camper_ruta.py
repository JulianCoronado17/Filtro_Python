import os
import json 

def asignar_camper_a_ruta(ruta_archivo):
    camper_id = input("Ingrese el ID del camper: ")
    ruta = input("Ingrese la ruta a la que desea asignar al camper: ").strip().lower()
    
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)
        
        if camper_id in campus['campers']:
            if ruta in campus['rutas']:
                campus['campers'][camper_id]['ruta'] = ruta
                with open(ruta_archivo, 'w') as archivo_json:
                    json.dump(campus, archivo_json, indent=4)
                print(f"\u001b[38;5;10mCamper '{camper_id}' asignado a la ruta '{ruta}' exitosamente.\u001b[0m")
            else:
                print("\u001b[38;5;196mLa ruta no existe.\u001b[0m")
        else:
            print("\u001b[38;5;196mID de camper no encontrado.\u001b[0m")
    else:
        print("Archivo campus.json no encontrado.")