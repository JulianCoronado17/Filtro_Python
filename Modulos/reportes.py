import json
import os

def listar_campers_inscritos(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo campus.json no encontrado.")
        return

    with open(ruta_archivo, 'r') as archivo_json:
        campus = json.load(archivo_json)

    inscritos = [camper_id for camper_id, datos in campus['campers'].items() if datos.get('estado') == 'Inscrito']

    if inscritos:
        print("Campers inscritos:")
        for camper_id in inscritos:
            print(f"ID: {camper_id}, Nombre: {campus['campers'][camper_id].get('nombre')}")
    else:
        print("No hay campers inscritos.")

def listar_campers_aprobados(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo campus.json no encontrado.")
        return

    with open(ruta_archivo, 'r') as archivo_json:
        campus = json.load(archivo_json)

    aprobados = [camper_id for camper_id, datos in campus['campers'].items() if datos.get('estado') == 'Aprobado']

    if aprobados:
        print("Campers aprobados:")
        for camper_id in aprobados:
            print(f"ID: {camper_id}, Nombre: {campus['campers'][camper_id].get('nombre')}")
    else:
        print("No hay campers aprobados.")

def listar_trainers(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo campus.json no encontrado.")
        return

    with open(ruta_archivo, 'r') as archivo_json:
        campus = json.load(archivo_json)

    if campus['trainers']:
        print("Trainers en CampusLands:")
        for trainer_id, datos in campus['trainers'].items():
            print(f"ID: {trainer_id}, Nombre: {datos.get('nombre')}")
    else:
        print("No hay trainers registrados.")

def listar_campers_bajo_rendimiento(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo campus.json no encontrado.")
        return

    with open(ruta_archivo, 'r') as archivo_json:
        campus = json.load(archivo_json)

    bajo_rendimiento = [camper_id for camper_id, datos in campus['campers'].items() if datos.get('estado') == 'Rendimiento Bajo']

    if bajo_rendimiento:
        print("Campers con bajo rendimiento:")
        for camper_id in bajo_rendimiento:
            print(f"ID: {camper_id}, Nombre: {campus['campers'][camper_id].get('nombre')}")
    else:
        print("No hay campers con bajo rendimiento.")

def listar_campers_trainers_por_ruta(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo campus.json no encontrado.")
        return

    with open(ruta_archivo, 'r') as archivo_json:
        campus = json.load(archivo_json)

    if 'matriculas' in campus:
        print("Campers y Trainers por Ruta:")
        for camper_id, matricula in campus['matriculas'].items():
            print(f"\nCamper ID: {camper_id}")
            for key, value in matricula.items():
                print(f"{key}: {value}")
    else:
        print("No hay matriculas registradas.")

def reporte_modulos(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo campus.json no encontrado.")
        return

    with open(ruta_archivo, 'r') as archivo_json:
        campus = json.load(archivo_json)

    reporte = {}

    for camper_id, datos in campus['campers'].items():
        if 'notas' in datos:
            for modulo, nota in datos['notas'].items():
                ruta = datos.get('ruta', 'Desconocida')
                trainer = datos.get('trainer', 'Desconocido')
                if ruta not in reporte:
                    reporte[ruta] = {}
                if modulo not in reporte[ruta]:
                    reporte[ruta][modulo] = {'Aprobados': 0, 'Perdidos': 0, 'Trainer': trainer}
                if nota >= 60:
                    reporte[ruta][modulo]['Aprobados'] += 1
                else:
                    reporte[ruta][modulo]['Perdidos'] += 1

    if reporte:
        print("Reporte de módulos por ruta y trainer:")
        for ruta, modulos in reporte.items():
            print(f"\nRuta: {ruta}")
            for modulo, resultados in modulos.items():
                print(f"Módulo: {modulo}, Trainer: {resultados['Trainer']}")
                print(f"Aprobados: {resultados['Aprobados']}, Perdidos: {resultados['Perdidos']}")
    else:
        print("No hay datos para generar el reporte.")
