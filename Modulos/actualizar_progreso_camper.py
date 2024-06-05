import os
import json

def actualizar_progreso_camper(ruta_archivo):
    camper_id = input("Ingrese el ID del camper: ")

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)

        if camper_id in campus['campers']:
            nuevo_progreso = input("Ingrese el nuevo progreso del camper: ")
            campus['campers'][camper_id]['progreso'] = nuevo_progreso
            with open(ruta_archivo, 'w') as archivo_json:
                json.dump(campus, archivo_json, indent=4)
            print("\u001b[38;5;10mProgreso actualizado.\u001b[0m")
        else:
            print("\u001b[38;5;196mID de camper no encontrado.\u001b[0m")
    else:
        print("Archivo campus.json no encontrado.")
        

def registrar_nota_camper(ruta_archivo):
    camper_id = input("Ingrese el ID del camper: ")
    nota_teorica = float(input("Ingrese la nota teórica del camper: "))
    nota_practica = float(input("Ingrese la nota práctica del camper: "))

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo_json:
            campus = json.load(archivo_json)

        if camper_id in campus['campers']:
            promedio = (nota_teorica + nota_practica) / 2
            campus['campers'][camper_id]['nota_teorica'] = nota_teorica
            campus['campers'][camper_id]['nota_practica'] = nota_practica
            campus['campers'][camper_id]['promedio'] = promedio

            if promedio >= 60:
                campus['campers'][camper_id]['estado'] = "Aprobado"
                
                # Asignar ruta a camper aprobado
                asignado = False
                for area, info in campus['areas'].items():
                    if 'campers' not in info:
                        info['campers'] = []
                    if len(info['campers']) < info['capacidad']:
                        info['campers'].append(camper_id)
                        campus['campers'][camper_id]['area'] = area
                        asignado = True
                        break
                
                if not asignado:
                    print("\u001b[38;5;196mNo hay capacidad disponible en ninguna área. El camper no ha sido asignado a ninguna ruta.\u001b[0m")
            else:
                campus['campers'][camper_id]['estado'] = "Reprobado"

            with open(ruta_archivo, 'w') as archivo_json:
                json.dump(campus, archivo_json, indent=4)
            print("\u001b[38;5;10mNotas registradas y estado actualizado exitosamente.\u001b[0m")
        else:
            print("\u001b[38;5;196mID de camper no encontrado.\u001b[0m")
    else:
        print("Archivo campus.json no encontrado.")
        

def registrar_notas_modulo(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo campus.json no encontrado.")
        return

    with open(ruta_archivo, 'r') as archivo_json:
        campus = json.load(archivo_json)

    camper_id = input("Ingrese el ID del camper: ")
    if camper_id not in campus['campers']:
        print("\u001b[38;5;196mID de camper no encontrado.\u001b[0m")
        return

    modulo = input("Ingrese el nombre del módulo: ")
    nota = float(input(f"Ingrese la nota del módulo {modulo}: "))

    if 'notas' not in campus['campers'][camper_id]:
        campus['campers'][camper_id]['notas'] = {}

    campus['campers'][camper_id]['notas'][modulo] = nota

    if nota < 60:
        campus['campers'][camper_id]['estado'] = 'Rendimiento Bajo'
        print("\u001b[38;5;196mEl camper ha sido marcado como Rendimiento Bajo.\u001b[0m")
    else:
        if all(n >= 60 for n in campus['campers'][camper_id]['notas'].values()):
            campus['campers'][camper_id]['estado'] = 'Aprobado'

    with open(ruta_archivo, 'w') as archivo_json:
        json.dump(campus, archivo_json, indent=4)
    print("\u001b[38;5;10mNota registrada y rendimiento evaluado con éxito.\u001b[0m")
    
def consultar_riesgo_alto(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo campus.json no encontrado.")
        return

    with open(ruta_archivo, 'r') as archivo_json:
        campus = json.load(archivo_json)

    riesgo_alto = [camper_id for camper_id, datos in campus['campers'].items() if datos.get('estado') == 'Rendimiento Bajo']

    if riesgo_alto:
        print("\u001b[38;5;196mCampers en Riesgo Alto:\u001b[0m")
        for camper_id in riesgo_alto:
            print(f"ID: {camper_id}, Nombre: {campus['campers'][camper_id].get('nombre')}")
    else:
        print("\u001b[38;5;10mNo hay campers en riesgo alto.\u001b[0m")
