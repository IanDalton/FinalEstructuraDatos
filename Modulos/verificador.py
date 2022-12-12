
ids_municipios = {"Ciudad Autonoma de Buenos Aires":"CAB","Santa Fe":"SFE","Tucuman":"TUC","Santa Cruz":"SCR",
"Cordoba":"CBA","Mendoza":"MZA","Buenos Aires":"BUE","Entre Rios":"ERI","Misiones":"MIS","Chubut":"CHU","Chaco":"CHA",
"La Pampa":"LPA","San Juan":"SJU","Jujuy":"JUJ","Salta":"SAL","La Rioja":"LRJ","Catamarca":"CAT","Neuquen":"NEU",
"Tierra del Fuego":"TDF","San Luis":"SLU","Santiago del Estero":"SGO","Formosa":"FOR","Rio Negro":"RNO",'Corrientes':'COR'}

def verificador_municipios(dict):
    return dict["municipio_id"][:3] == ids_municipios[dict["provincia"]]
