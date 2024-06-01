import json

def inscribir():
    n_documento=input("Ingrese el número de documento: ")
    nombres=input("Ingrese sus nombres: ")
    apellidos=input("Ingrese sus apellidos: ")
    direccion=input("Ingrese su driección: ")
    acudiente=input("Ingrese el nombre de su acudiente : ")
    celular=input("Ingrese el número de celular: ")
    fijo=input("Ingrese el número fijo: ")
    riesgo=False
    dic={n_documento:{'Nombre':nombres,
         'Apellidos':apellidos,'Direccion':direccion,
         'Acudiente': acudiente,'Celular': celular,
         'Fijo':fijo,'Estado':"","Riesgo":riesgo}}
    
    camper=json.dumps(dic,indent=4)

    file=open("campers.json","a")

    file.write(camper)
    file.close

  
    


    