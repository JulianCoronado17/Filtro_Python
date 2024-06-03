import json
import os
from datetime import datetime

def registrar_matricula(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo campus.json no encontrado.")
        return

    with open(ruta_archivo, 'r') as archivo_json:
        campus = json.load(archivo_json)

    camper_id = input("Ingrese el ID del camper aprobado: ")
    if camper_id not in campus['campers'] or campus['campers'][camper_id]['estado'] != 'Aprobado':
        print("Camper no encontrado o no aprobado.")
        return

    trainer_id = input("Ingrese el ID del trainer encargado: ")
    if trainer_id not in campus['trainers']:
        print("Trainer no encontrado.")
        return

    ruta_nombre = input("Ingrese la ruta de entrenamiento asignada: ")
    if ruta_nombre not in campus['rutas']:
        print("Ruta no encontrada.")
        return

    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_finalizacion = input("Ingrese la fecha de finalización (YYYY-MM-DD): ")

    try:
        datetime.strptime(fecha_inicio, "%Y-%m-%d")
        datetime.strptime(fecha_finalizacion, "%Y-%m-%d")
    except ValueError:
        print("Formato de fecha inválido.")
        return

    area_asignada = None
    for area, detalles in campus['areas'].items():
        if len(detalles['campers']) < detalles['capacidad']:
            area_asignada = area
            break

    if not area_asignada:
        print("No hay áreas disponibles con capacidad suficiente.")
        return

    matricula_id = f"mat_{len(campus['matricula']) + 1}"
    campus['matricula'][matricula_id] = {
        'camper_id': camper_id,
        'trainer_id': trainer_id,
        'ruta': ruta_nombre,
        'fecha_inicio': fecha_inicio,
        'fecha_finalizacion': fecha_finalizacion,
        'area': area_asignada
    }

    campus['areas'][area_asignada]['campers'].append(camper_id)

    with open(ruta_archivo, 'w') as archivo_json:
        json.dump(campus, archivo_json, indent=4)

    print("Matrícula registrada con éxito.")



def ver_matriculas(ruta_archivo):
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)

        if 'matriculas' in campus:
            print("Matriculas registradas:")
            for camper_id, matricula in campus['matriculas'].items():
                print(f"\nCamper ID: {camper_id}")
                for key, value in matricula.items():
                    print(f"{key}: {value}")
        else:
            print("No hay matrículas registradas.")
    else:
        print("Archivo campus.json no encontrado.")