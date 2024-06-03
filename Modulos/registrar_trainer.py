import os
import json

def registrar_nuevo_trainer(ruta_archivo):
    nuevo_trainer = {}
    trainer_id = input("Ingrese el ID del nuevo trainer: ")
    nuevo_trainer['nombre'] = input("Ingrese el nombre del trainer: ")
    nuevo_trainer['especialidad'] = input("Ingrese la especialidad del trainer: ")
    nuevo_trainer['area'] = input("Ingrese el área asignada del trainer: ")

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)
        
        campus['trainers'][trainer_id] = nuevo_trainer
        
        with open(ruta_archivo, 'w') as archivo_json:
            json.dump(campus, archivo_json, indent=4)
        print("Nuevo trainer registrado exitosamente.")
    else:
        print("Archivo campus.json no encontrado.")