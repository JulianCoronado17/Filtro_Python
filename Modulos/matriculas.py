import json
import os
from datetime import datetime

def registrar_matricula(ruta_archivo):
    camper_id = input("Ingrese el ID del camper: ")
    trainer_id = input("Ingrese el ID del trainer: ")
    ruta_entrenamiento = input("Ingrese la ruta de entrenamiento: ")
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de finalización (YYYY-MM-DD): ")

    if not os.path.exists(ruta_archivo):
        print("Archivo campus.json no encontrado.")
        return

    with open(ruta_archivo, 'r') as archivo_json:
        campus = json.load(archivo_json)

    # Verificar que el camper está aprobado
    if camper_id not in campus['campers']:
        print("\u001b[38;5;196mID de camper no encontrado.\u001b[0m")
        return
    if campus['campers'][camper_id]['estado'] != 'Aprobado':
        print("\u001b[38;5;196mEl camper no está aprobado.\u001b[0m")
        return

    # Asignar área de entrenamiento
    area_asignada = None
    for area, detalles in campus['areas'].items():
        if 'campers' not in detalles:
            detalles['campers'] = []
        if len(detalles['campers']) < detalles['capacidad']:
            area_asignada = area
            break

    if not area_asignada:
        print("\u001b[38;5;196mNo hay áreas disponibles con capacidad suficiente.\u001b[0m")
        return

    # Asignar la matrícula
    matricula_id = f"{camper_id}_{ruta_entrenamiento}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    campus['matricula'][matricula_id] = {
        'camper_id': camper_id,
        'trainer_id': trainer_id,
        'ruta_entrenamiento': ruta_entrenamiento,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'area_asignada': area_asignada
    }
    campus['areas'][area_asignada]['campers'].append(camper_id)

    with open(ruta_archivo, 'w') as archivo_json:
        json.dump(campus, archivo_json, indent=4)

    print(f"\u001b[38;5;10mMatrícula registrada con éxito. ID de matrícula: {matricula_id}\u001b[0m")





def ver_matriculas(ruta_archivo):
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)

        if 'matricula' in campus and campus['matricula']:
            print("\u001b[38;5;10mMatrículas registradas:\u001b[0m")
            for matricula_id, matricula in campus['matricula'].items():
                print(f"\u001b[38;5;10m\nMatrícula ID: {matricula_id}\u001b[0m")
                for key, value in matricula.items():
                    print(f"\u001b[38;5;10m{key}\u001b[0m: \u001b[38;5;10m{value}\u001b[0m")
        else:
            print("\u001b[38;5;196mNo hay matrículas registradas.\u001b[0m")
    else:
        print("Archivo campus.json no encontrado.")
