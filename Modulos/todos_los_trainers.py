import os
import json

def ver_todos_los_trainers(ruta_archivo):
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)
        
        print("\u001b[38;5;10mInformación de todos los trainers:\u001b[0m")
        for trainer_id, info in campus['trainers'].items():
            print(f"\nID: {trainer_id}")
            for key, value in info.items():
                print(f"{key}: {value}")
    else:
        print("Archivo campus.json no encontrado.")