import csv 
from clases import * 

#provincia_id,municipio_id,id_departamento,municipio,provincia,departamento

ids_municipios = {"Ciudad Autonoma de Buenos Aires":"CBA","Santa Fe":"SFE","Tucuman":"TUC","Santa Cruz":"SCR",
"Cordoba":"COR","Mendoza":"MZA","Buenos Aires":"BUE","Entre Rios":"ERI","Misiones":"MIS","Chubut":"CHU","Chaco":"CHA",
"La Pampa":"LPA","San Juan":"SJU","Jujuy":"JUJ","Salta":"SAL","La Rioja":"LRJ","Catamarca":"CAT","Neuquen":"NEU",
"Tierra del Fuego":"TDF","San Luis":"SLU","Santiago del Estero":"SGO","Formosa":"FOR","Rio Negro":"RNO"}

def loadcsv(path: str):
    lista_errores = []
    with open(path, "r") as file:  
        for val in csv.DictReader(file):
            for keys,values in ids_municipios.items():
                if val["provincia"] == keys and val["municipio_id"][:3] == values: #no entra nunca a este ciclo, pero si lo corro por separado funciona bien
                    pass
                    # Departamento(val["id_departamento"],val["departamento"],val["municipio"]) --> TENGO QUE HACER ESTO PARA GUARDAR LA INFO
                    # Municipio(val["provincia_id"],val["municipio"],val["provincia"])
                    # Provincia(val["provincia"],"Argentina")
                else:
                    lista_errores.append(val) #agrega cada vez que hace un ciclo de items en la lista errores. Nose como arreglarlo 
            break
        


if __name__ == "__main__":
    loadcsv("C:/Users/Usuario/OneDrive/Documentos/GITHUB/FinalEstructuraDatos/Datos/municipios.csv")


