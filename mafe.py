import modulos.camperModule as cams
import os
import modulos.pruebaModule as prb

camper={
    "01": {
        "nombre": "Maria",
        "apellido": "Gamez",
        "direccion": "ddddd",
        "acudiente": "Diana",
        "telefonos": [
            {
                "celular": "1111"
            }
        ],
        "estado": "inscrito",
        "sub-estado": "",
        "pruebas": {
            "iniciales": {
                "practica": "50",
                "teorica": "86"
            }
        },
        "ruta": "",
        "trainer": "",
        "fecha": {
            "inicio": "aaaa",
            "final": ""
        },
        "area": ""
    },
    "02": {
        "nombre": "Julian",
        "apellido": "Piñeros",
        "direccion": "mmmmm",
        "acudiente": "Andrea",
        "telefonos": [
            {
                "celular": "22222"
            }
        ],
        "estado": "aprobado",
        "sub-estado": "",
        "pruebas": {
            "iniciales": {
                "practica": "90",
                "teorica": "60"
            }
        },
        "ruta": "",
        "trainer": "",
        "fecha": {
            "inicio": "aaaa",
            "final": ""
        },
        "area": ""
    }
}
rutas={
    'java':{
        'fundamentos':{'IntrAlgoritmia', 'PSeInt', 'Python'},
        'web':{'HTML', 'CSS', 'Bootstrap'},
        'lenguajeformal':{'Java', 'JavaScript', 'C#'},
        'basedatos':{
            'Mysql':{'SGDBprincipal','SGDBalternativo'}, 
            'MongoDb':{'SGDBprincipal','SGDBalternativo'},
            'Postgresql':{'SGDBprincipal','SGDBalternativo'}
        },
        'backend':{'NetCore', 'Spring Boot', 'NodeJS', 'Express'}
    },
    'nodejs':{
        'fundamentos':{'IntrAlgoritmia', 'PSeInt', 'Python'},
        'web':{'HTML', 'CSS', 'Bootstrap'},
        'lenguajeformal':{'Java', 'JavaScript', 'C#'},
        'basedatos':{
            'Mysql':{'SGDBprincipal','SGDBalternativo'}, 
            'MongoDb':{'SGDBprincipal','SGDBalternativo'},
            'Postgresql':{'SGDBprincipal','SGDBalternativo'}
        },
        'backend':{'NetCore', 'Spring Boot', 'NodeJS', 'Express'}
    },
    
    'netcore':{
        'fundamentos':{'IntrAlgoritmia', 'PSeInt', 'Python'},
        'web':{'HTML', 'CSS', 'Bootstrap'},
        'lenguajeformal':{'Java', 'JavaScript', 'C#'},
        'basedatos':{
            'Mysql':{'SGDBprincipal','SGDBalternativo'}, 
            'MongoDb':{'SGDBprincipal','SGDBalternativo'},
            'Postgresql':{'SGDBprincipal','SGDBalternativo'}
        },
        'backend':{'NetCore', 'Spring Boot', 'NodeJS', 'Express'}
    }
}

trainers={
    'Miguel':{
        'horarios':{
            '6am',
            '10am',
            '2pm'
            },
        'ruta':'nodeJS'
        },
    'Jholver':{
        'horarios':{
            '6am',
            '10am'
            '2pm'
            },
        'ruta':'Java'
        },
    'Pedro':{
        'horarios':{
            '6am',
            '10am'
            '2pm'
            },
        'ruta':'Netcore'
        }
    }

matricula={}
areas={
    'sputnik':{
        'nombre':'sputnik',
        'capacidad':33
    },
    'apolo':{
        'nombre':'apolo',
        'capacidad':33
    },
    'artemis':{
        'nombre':'artemis',
        'capacidad':33
    }
}