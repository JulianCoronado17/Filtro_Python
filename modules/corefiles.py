import json
import os
#Crear una base de datos donde se guarde el json
BASE_DATA="data/"

#CHECKFILE ------> Verificar si un archivo.json existe
#SOLO SE LLAMA UNA VEZ EN MAIN

#1.A la funcion le pasaremos los argumentos de Archivo(por defecto),DiccionarioGlobal(llamandolo por el nombre con el que esta en MAIN)
def checkFile(Archivo,dictGlobal):
    #2.si el archivo no esta(LLAMO LA BASE DE DATOS+CREAR EL Archivo DENTRO DE LA BASE)
    if(not(os.path.isfile(BASE_DATA+Archivo))):
        #3.Abrir (BASE DE DATOS + ARCHIVO, con atributos de ESCRITURA) con un alias
        with open(BASE_DATA + Archivo,"w+") as createFile:
            #4.subir al Json el(DICCIONARIO GLOBAL, ALIAS,INDENTACION)
            json.dump(dictGlobal, createFile, indent=4)


#UPDATEFILE ------> Subir cada actualizacion al archivo.json

#1.A la funcion le damos los argumentos por defecto de archivo,diccionario independiente de sus nombres reales
def UpdateFile(Archivo,Diccionario):
    #2.Abrir con atributos de escritura el archivo
    with open(Archivo,"w+") as Upload:
        #3.Subir los cambios de json(AL DICCIONARIO, CON EL ALIAS, IDENTACION)
        json.dump(Diccionario, Upload, indent=4)


#READFILE ------> Leer o cargar todo lo que este en el Archivo.json
        
#1.A la funcion le pasamos unicamente el argumento de Archivo 
def ReadFile():
    with open(BASE_DATA+Archivo,"r+") as read:
        return json.load(read.read())
        