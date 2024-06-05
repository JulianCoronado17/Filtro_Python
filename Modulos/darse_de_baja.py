import os
import json

def darse_de_baja(ruta_archivo):
    camper_id = input("Ingrese su ID de camper: ")

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)

        if camper_id in campus['campers']:
            confirmacion = input("¿\u001b[38;5;196mEstá seguro que quiere darse de baja\u001b[0m? (si/no): ")
            if confirmacion.lower() == 'si':
                del campus['campers'][camper_id]
                with open(ruta_archivo, 'w') as archivo_json:
                    json.dump(campus, archivo_json, indent=4)
                print("\u001b[38;5;10mSe ha dado de baja exitosamente.\u001b[0m")
            else:
                print("\u001b[38;5;10mOperación cancelada.\u001b[0m")
        else:
            print("\u001b[38;5;196mID de camper no encontrado.\u001b[0m")
    else:
        print("Archivo campus.json no encontrado.")
        
def eliminar_camper(ruta_archivo):
    camper_id = input("Ingrese el ID del camper que desea eliminar: ")

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)

        if camper_id in campus['campers']:
            del campus['campers'][camper_id]
            with open(ruta_archivo, 'w') as archivo_json:
                json.dump(campus, archivo_json, indent=4)
            print("\u001b[38;5;10mCamper eliminado exitosamente.\u001b[0m")
        else:
            print("\u001b[38;5;196mID de camper no encontrado.\u001b[0m")
    else:
        print("Archivo campus.json no encontrado.")