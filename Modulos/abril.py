import csv 
from clases import * 

#provincia_id,municipio_id,id_departamento,municipio,provincia,departamento

ids_municipios = {"Ciudad Autonoma de Buenos Aires":"CAB","Santa Fe":"SFE","Tucuman":"TUC","Santa Cruz":"SCR",
"Cordoba":"CBA","Mendoza":"MZA","Buenos Aires":"BUE","Entre Rios":"ERI","Misiones":"MIS","Chubut":"CHU","Chaco":"CHA",
"La Pampa":"LPA","San Juan":"SJU","Jujuy":"JUJ","Salta":"SAL","La Rioja":"LRJ","Catamarca":"CAT","Neuquen":"NEU",
"Tierra del Fuego":"TDF","San Luis":"SLU","Santiago del Estero":"SGO","Formosa":"FOR","Rio Negro":"RNO",'Corrientes':'COR'}

ides = set()
def loadcsv(path: str):
    lista_errores = []
    lista_ok = []
    with open(path, "r") as file:  
        for val in csv.DictReader(file):
            if val["municipio_id"][:3] == ids_municipios[val["provincia"]]:
                lista_ok.append(val)
                pass
                # Departamento(val["id_departamento"],val["departamento"],val["municipio"]) 
                # Municipio(val["provincia_id"],val["municipio"],val["provincia"])
                # Provincia(val["provincia"],"Argentina")
            else:
                lista_errores.append(val) 
    print(lista_errores)
    with open('errores.csv','w',newline='') as arch:
        fieldnames = lista_errores[0].keys()
        writer = csv.DictWriter(arch,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(lista_errores)
    with open('ok.csv','w',newline='') as arch:
        fieldnames = lista_errores[0].keys()
        writer = csv.DictWriter(arch,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(lista_ok)
        


if __name__ == "__main__":
    loadcsv("Datos\municipios.csv")

    

#{'', 'TDF', 'CBA', 'COR', 'SJU', 'SCR', 'JUJ', 'ERI', 'MIS', 'CAB', 'BUE', 'LAP', 'MZA', 'SLU', 'LRJ', 'RNO', 'CHA', 'CHU', 'SAL', 'FOR', 'TUC', 'SFE', 'NEU', 'CAT', 'SGO'} 25