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
            print("Progreso actualizado.")
        else:
            print("ID de camper no encontrado.")
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
                    print("No hay capacidad disponible en ninguna área. El camper no ha sido asignado a ninguna ruta.")
            else:
                campus['campers'][camper_id]['estado'] = "Reprobado"

            with open(ruta_archivo, 'w') as archivo_json:
                json.dump(campus, archivo_json, indent=4)
            print("Notas registradas y estado actualizado exitosamente.")
        else:
            print("ID de camper no encontrado.")
    else:
        print("Archivo campus.json no encontrado.")