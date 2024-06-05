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
1-\033[35;1mCamper\033[0m
2-\033[35;1mTrainer\033[0m
3-\033[35;1mCoordinador\033[0m
0-\033[35;1mSalir\033[0m
"""
menu_camper="""
1-\033[31;1mIncribirse\033[0m
2-\033[31;1mVer Información del Camper\033[0m
3-\033[31;1mActualizar Información del Camper\033[0m
4-\033[31;1mVer Estado del Proceso\033[0m
5-\033[31;1mVer Rutas Disponibles\033[0m
6-\033[31;1mDarse de Baja\033[0m
"""
menu_trainer="""
1-\033[36;1mVer la información detallada de un camper\033[0m
2-\033[36;1mActualizar el progreso de un camper en su ruta\033[0m
3-\033[36;1mVer el estado del proceso de un camper\033[0m
4-\033[36;1mAgregar una nueva ruta de entrenamiento\033[0m
5-\033[36;1mAsignar campers a una ruta específica\033[0m
"""


menu_coordinador = """
1. \033[33;1mRegistrar nuevo trainer\033[0m
2. \033[33;1mAsignar área a trainer\033[0m
3. \033[33;1mVer información de todos los trainers\033[0m
4. \033[33;1mActualizar estado y riesgo de camper\033[0m
5. \033[33;1mVer todas las rutas disponibles\033[0m
6. \033[33;1mEliminar camper\033[0m
7. \033[33;1mRegistrar nota de camper\033[0m
8. \033[33;1mInscribir camper\033[0m
9. \033[33;1mCrear nueva ruta\033[0m
10. \033[33;1mRegistrar matricula\033[0m
11. \033[33;1mVer matriculas\033[0m
12. \033[33;1mRegistrar notas por módulo y evaluar rendimiento\033[0m
13. \033[33;1mConsultar campers en riesgo alto\033[0m
14. \033[34;4mReportes\033[0m
"""
menu_reportes = """
1-\u001b[38;5;51mListar campers inscritos\u001b[0m
2-\u001b[38;5;86mListar campers aprobados\u001b[0m
3-\u001b[38;5;25mListar trainers\u001b[0m
4-\u001b[38;5;18mListar campers con bajo rendimiento\u001b[0m
5-\u001b[38;5;165mListar campers y trainers por ruta\u001b[0m
6-\u001b[38;5;42mReporte de módulos por ruta y trainer\u001b[0m
"""

ruta_carpeta = 'Data'
ruta_archivo = os.path.join(ruta_carpeta, 'campus.json')

# if not os.path.exists(ruta_archivo):
#     campus = {
#         'campers': {},
#         'trainers': {},
#         'areas': {
#             'nodejs': {'capacidad': 33, 'campers': []},
#             'java': {'capacidad': 33, 'campers': []},
#             'netcore': {'capacidad': 33, 'campers': []}
#         },
#         'rutas': ['nodejs', 'java', 'netcore']
#     }
#     with open(ruta_archivo, 'w') as archivo_json:
#         json.dump(campus, archivo_json, indent=4)

while True:
    print("                                    ")
    print("                                    ")
    print("                                    ")
    print("""\033[36;3;1mBIENVENIDO A CAMPUSLANDS\033[0m""")
    
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
            ver_informacion_camper(ruta_archivo)
        elif opc_camper == "3":
            actualizar_informacion_camper(ruta_archivo)
        elif opc_camper == "4":
            ver_estado_proceso(ruta_archivo)
        elif opc_camper == "5":
            ver_rutas_disponibles(ruta_archivo)
        elif opc_camper == "6":
            darse_de_baja(ruta_archivo)
        else:
            print("\u001b[38;5;196mEscoja un opcion existente\u001b[0m")
            
            
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
                print("\u001b[38;5;196mEscoja una opción existente\u001b[0m")
                
    elif opc=="0":
        print("Salio")
        break                         
    else:
        print("\u001b[38;5;196mEscoja un rol existente\u001b[0m")


