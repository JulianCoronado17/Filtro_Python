from menu_principal import*
from inscribir import *
import menu_camper

while True:
    print(menu)
    opc=input("Ingrese una opcion: ")
    
    if opc=="1":
        while True:
            print(menu_camper.menu)
            opc_camper=input("Escoja una opción: ")
            if opc_camper =="1":
                inscribir()
                print("\033[34mInscripcion exitosa\033[0m")
                break
            else:
                print("Selecione una opcion que exista")    
    else:
        print("Selecione una opcion que exista")    
       
            
        