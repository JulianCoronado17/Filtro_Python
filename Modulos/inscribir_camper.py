import os
import json

def addCamper(campers:dict):
    id=input("Ingrese ID: ")
    nombre=input("Ingrese Nombre: ")
    apellido=input("Ingrese Apellido : ")
    direccion=input("Ingrese Direccion: ")
    acudiente=input("Ingrese Acudiente: ")
    celular=input("Ingrese número de celular: ")
    fijo=input("Ingrese número de Fijo: ")
    estado="Inscrito"
    riesgo=False
    camper={
        'id':id,
        'nombre':nombre,
        'apellido':apellido,
        'direccion':direccion,
        'acudiente':acudiente,
        'celular':celular,
        'fijo':fijo,
        'estado':estado,
        'riesgo':riesgo   
    }
    campers.update({id:camper})
    print("""\033[32mRegistro exitoso!\033[0m""")

def inscribir_camper(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo campus.json no encontrado.")
        return

    with open(ruta_archivo, 'r') as archivo_json:
        campus = json.load(archivo_json)

    camper_id = input("Ingrese el ID del nuevo camper: ")
    nombre = input("Ingrese el nombre del nuevo camper: ")

    nuevo_camper = {
        'nombre': nombre,
        'estado': 'Inscrito'
    }

    campus['campers'][camper_id] = nuevo_camper

    # Asignar área al camper
    area_asignada = None
    for area, info in campus['areas'].items():
        if len(info.get('campers', [])) < info.get('capacidad', 33):  # Assuming 33 is the default capacity
            area_asignada = area
            break

    if area_asignada:
        if 'campers' not in campus['areas'][area_asignada]:
            campus['areas'][area_asignada]['campers'] = []
        campus['areas'][area_asignada]['campers'].append(camper_id)
        print(f"Camper {nombre} asignado al área {area_asignada}.")
    else:
        print("No hay áreas disponibles para asignar al nuevo camper.")

    with open(ruta_archivo, 'w') as archivo_json:
        json.dump(campus, archivo_json, indent=4)

    print(f"Camper {nombre} registrado con éxito.")