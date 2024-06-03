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

def inscribir_camper(campus):
    nuevo_camper = {}
    camper_id = input("Ingrese el ID del camper: ")
    nuevo_camper['nombre'] = input("Ingrese el nombre del camper: ")
    nuevo_camper['edad'] = input("Ingrese la edad del camper: ")
    nuevo_camper['ruta'] = input("Ingrese la ruta del camper (nodejs/java/netcore): ")

    # Asignar área de entrenamiento
    asignado = False
    for area, info in campus['areas'].items():
        if 'campers' not in info:
            info['campers'] = []
        if len(info['campers']) < info['capacidad']:
            info['campers'].append(camper_id)
            nuevo_camper['area'] = area
            asignado = True
            break

    if not asignado:
        print("No hay capacidad disponible en ninguna área.")
        return

    campus['campers'][camper_id] = nuevo_camper

    return campus