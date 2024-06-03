import json
import Modulos.inscribir_camper as camp
from Modulos.inscribir_camper import*
from Modulos.ver_info_camper import*
from Modulos.actualizar_info_camper import*
from Modulos.ver_estado import *
from Modulos.darse_de_baja import*
from Modulos.rutas import*
from Modulos.resgi_nueva_ruta import*
from Modulos.ver_info_camper_trainer import*
from Modulos.actualizar_progreso_camper import*
from Modulos.ver_estado_proceso_camper import*
from Modulos.asig_camper_ruta import*
from Modulos.registrar_trainer import*
from Modulos.asignar_area_trainer import*
from Modulos.todos_los_trainers import*
from Modulos.act_riesgo_camper import*
from Modulos.matriculas import*
from Modulos.reportes import*
import Modulos.rutas as rutas

import os

campus = {
    'campers':{},
    'rutas':{
        'nodejs':{
            'fundamentos':{
                'introduccion_algoritmia':{},
                'pseint':{},
                'python':{}
            },
            'web':{
                'html':{},
                'css':{},
                'bootstrap':{}
            },
            'progformal':{
                'java':{},
                'javascript':{},
                'csharp':{}
            },
            'baseDatos':{
                'principal': 'Mysql',
                'alternativo': 'MongoDb',
                'mysql':{},
                'mongodb':{},
                'postgresql':{}
            },
            'backend':{
                'netcore':{},
                'spring_boot':{},
                'nodejs':{},
                'express':{}
            },
        },
        'java':{
            'fundamentos':{
                'introduccion_algoritmia':{},
                'pseint':{},
                'python':{}
            },
            'web':{
                'html':{},
                'css':{},
                'bootstrap':{}
            },
            'progformal':{
                'java':{},
                'javascript':{},
                'csharp':{}
            },
            'baseDatos':{
                'principal': 'Postgresql',
                'alternativo': 'Mysql',
                'mysql':{},
                'mongodb':{},
                'postgresql':{}
            },
            'backend':{
                'netcore':{},
                'spring_boot':{},
                'nodejs':{},
                'express':{}
            },
        },
        'netcore':{
            'fundamentos':{
                'introduccion_algoritmia':{},
                'pseint':{},
                'python':{}
            },
            'web':{
                'html':{},
                'css':{},
                'bootstrap':{}
            },
            'progformal':{
                'java':{},
                'javascript':{},
                'csharp':{}
            },
            'baseDatos':{
                'principal': 'MongoDb',
                'alternativo': 'Mysql',
                'mysql':{},
                'mongodb':{},
                'postgresql':{}
            },
            'backend':{
                'netcore':{},
                'spring_boot':{},
                'nodejs':{},
                'express':{}
            },
        }
    },
    'areas':{
        'apolo':{
            'nombre':'Apolo',
            'capacidad':33,
            'campers':[]
        },
        'artemis':{
            'nombre':'Artemis',
            'capacidad':35,
            'campers':[]
        },
        'sputnik':{
            'nombre':'Sputnik',
            'capacidad':33,
            'campers':[]
        }
    },
    'trainers':{},
    'matricula':{},
}


menu_principal="""
1. Camper
2. Trainer
3. Coordinador
0. Salir
"""
menu_camper="""
1. Incribirse
2. Ver Información del Camper
3. Actualizar Información del Camper
4. Ver Estado del Proceso
5. Ver Rutas Disponibles
6. Darse de Baja
"""
menu_trainer="""
1. Agregar una nueva ruta de entrenamiento
2. Asignar campers a una ruta específica
3. Ver la información detallada de un camper
4. Actualizar el progreso de un camper en su ruta
5. Ver el estado del proceso de un camper
6. Ver información detallada de todos los trainers
"""

menu_coordinador = """
1. Registrar nuevo trainer
2. Asignar área a trainer
3. Ver información de todos los trainers
4. Actualizar estado y riesgo de camper
5. Ver todas las rutas disponibles
6. Eliminar camper
7. Registrar nota de camper
8. Inscribir camper
9. Crear nueva ruta
10. Registrar matricula
11. Ver matriculas
12. Registrar notas por módulo y evaluar rendimiento
13. Consultar campers en riesgo alto
14. Reportes
"""
menu_reportes = """
1. Listar campers inscritos
2. Listar campers aprobados
3. Listar trainers
4. Listar campers con bajo rendimiento
5. Listar campers y trainers por ruta
6. Reporte de módulos por ruta y trainer
"""

ruta_carpeta = 'Data'
ruta_archivo = os.path.join(ruta_carpeta, 'campus.json')

if not os.path.exists(ruta_archivo):
    campus = {
        'campers': {},
        'trainers': {},
        'areas': {
            'nodejs': {'capacidad': 33, 'campers': []},
            'java': {'capacidad': 33, 'campers': []},
            'netcore': {'capacidad': 33, 'campers': []}
        },
        'rutas': ['nodejs', 'java', 'netcore']
    }
    with open(ruta_archivo, 'w') as archivo_json:
        json.dump(campus, archivo_json, indent=4)

while True:
    print("""\033[36mBIENVENIDO A CAMPUSLANDS\033[0m""")
    print(menu_principal)
    opc=input("Escoja cual es su rol: ")
    if opc == "1":
        print(menu_camper)
        opc_camper=input("Escoja una opcion: ")
    
        if opc_camper=="1" :
            
            if not os.path.exists(ruta_carpeta):
                os.makedirs(ruta_carpeta)
            if os.path.exists(ruta_archivo):
                with open(ruta_archivo, 'r') as archivo_json:
                    campus = json.load(archivo_json)

            camp.addCamper(campus['campers'])

            with open(ruta_archivo, "w") as archivo_json:
                json.dump(campus, archivo_json, indent=4)           
        
        elif opc_camper == "2":
            # Implementar función para ver información del camper
            rutas.crear_nueva_ruta(ruta_nombre, ruta_archivo)
        elif opc_camper == "3":
            # Implementar función para actualizar información del camper
            actualizar_informacion_camper(ruta_archivo)
        elif opc_camper == "4":
            # Implementar función para ver estado del proceso
            ver_estado_proceso(ruta_archivo)
        elif opc_camper == "5":
            # Implementar función para ver rutas disponibles
            ver_rutas_disponibles(ruta_archivo)
        elif opc_camper == "6":
            # Implementar función para darse de baja
            darse_de_baja(ruta_archivo)
        else:
            print("Escoja un opcion existente")
            
            
    elif opc=="2":
        print(menu_trainer)
        opc_trainer=input("Escoja una opcion: ")
        if opc_trainer == "1":
            ver_info_camper_trainer(ruta_archivo)
        elif opc_trainer == "2":
            actualizar_progreso_camper(ruta_archivo)
        elif opc_trainer == "3":
            ver_estado_proceso_camper(ruta_archivo)
        elif opc_trainer == "4":
            registrar_nueva_ruta(ruta_archivo)
        elif opc_trainer == "5":
            asignar_camper_a_ruta(ruta_archivo)
        else:
            print("Escoja una opción existente")
            
    elif opc == "3":
        print(menu_coordinador)
        opc_coordinador = input("Escoja una opción: ")

        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r') as archivo_json:
                campus = json.load(archivo_json)

        if opc_coordinador == "1":
            registrar_nuevo_trainer(ruta_archivo)
        elif opc_coordinador == "2":
            asignar_area_a_trainer(ruta_archivo)
        elif opc_coordinador == "3":
            ver_todos_los_trainers(ruta_archivo)
        elif opc_coordinador == "4":
            actualizar_estado_riesgo_camper(ruta_archivo)
        elif opc_coordinador == "5":
            ver_todas_las_rutas(ruta_archivo)
        elif opc_coordinador == "6":
            eliminar_camper(ruta_archivo)
        elif opc_coordinador == "7":
            registrar_nota_camper(ruta_archivo)
        elif opc_coordinador == "8":
            inscribir_camper(ruta_archivo)
        elif opc_coordinador == "9":
            ruta_nombre = input("Ingrese el nombre de la nueva ruta de entrenamiento: ")
            rutas.crear_nueva_ruta(ruta_nombre, ruta_archivo)  # Pasa la ruta del archivo aquí
        elif opc_coordinador=="10":
            registrar_matricula(ruta_archivo)
        elif opc_coordinador == "11":
            ver_matriculas(ruta_archivo)
        elif opc_coordinador == "12":
            registrar_notas_modulo(ruta_archivo)
        elif opc_coordinador =="13":
            consultar_riesgo_alto(ruta_archivo)
            
            
        elif opc_coordinador == "14":
            
            print(menu_reportes)
            opc_reporte=input("Escoja que desea hacer: ")
            if opc_reporte == "1":
                listar_campers_inscritos(ruta_archivo)
            elif opc_reporte == "2":
                listar_campers_aprobados(ruta_archivo)
            elif opc_reporte == "3":
                listar_trainers(ruta_archivo)
            elif opc_reporte == "4":
                listar_campers_bajo_rendimiento(ruta_archivo)
            elif opc_reporte == "5":
                listar_campers_trainers_por_ruta(ruta_archivo)
            elif opc_reporte == "6":
                reporte_modulos(ruta_archivo)
            else:
                print("Escoja una opción existente")
                
    elif opc=="0":
        print("Salio")
        break                         
    else:
        print("Escoja un rol existente")

#Arreglar agregar matricula, deje la linea pa chat gpt ya escrita, limite reestablecido para las 6:47 am
