import json
import os

def registrar_nueva_ruta(ruta_archivo):
    nueva_ruta = input("Ingrese el nombre de la nueva ruta: ").strip().lower()
    
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)
        
        if nueva_ruta not in campus['rutas']:
            campus['rutas'][nueva_ruta] = {
                'fundamentos': {},
                'web': {},
                'progformal': {},
                'baseDatos': {},
                'backend': {},
            }
            with open(ruta_archivo, 'w') as archivo_json:
                json.dump(campus, archivo_json, indent=4)
            print(f"\u001b[38;5;10mNueva ruta '{nueva_ruta}' registrada exitosamente.\u001b[0m")
        else:
            print("\u001b[38;5;196mLa ruta ya existe.\u001b[0m")
    else:
        print("Archivo campus.json no encontrado.")