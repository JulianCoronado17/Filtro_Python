import os
import json


def ver_rutas_disponibles(ruta_archivo):
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)

        print("\u001b[38;5;10mRutas de entrenamiento disponibles:\u001b[0m")
        for ruta in campus['rutas']:
            print(f"- {ruta.capitalize()}")
    else:
        print("Archivo campus.json no encontrado.")


def ver_todas_las_rutas(ruta_archivo):
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)
        
        print("\u001b[38;5;10mRutas disponibles:\u001b[0m")
        for ruta in campus['rutas']:
            print(f"Ruta: {ruta}")
    else:
        print("Archivo campus.json no encontrado.")
        

def crear_nueva_ruta(ruta_nombre, ruta_archivo):
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)
    else:
        print("Archivo campus.json no encontrado.")
        return

    if ruta_nombre in campus['rutas']:
        print("\u001b[38;5;196mLa ruta ya existe.\u001b[0m")
        return

    campus['rutas'][ruta_nombre] = {
        'fundamentos': {
            'introduccion_algoritmia': {},
            'pseint': {},
            'python': {}
        },
        'web': {
            'html': {},
            'css': {},
            'bootstrap': {}
        },
        'progformal': {
            'java': {},
            'javascript': {},
            'csharp': {}
        },
        'baseDatos': {
            'principal': 'Mysql',
            'alternativo': 'MongoDb',
            'mysql': {},
            'mongodb': {},
            'postgresql': {}
        },
        'backend': {
            'netcore': {},
            'spring_boot': {},
            'nodejs': {},
            'express': {}
        },
    }

    with open(ruta_archivo, 'w') as archivo_json:
        json.dump(campus, archivo_json, indent=4)

    print(f"\u001b[38;5;10mRuta {ruta_nombre} creada con éxito.\u001b[0m")



  