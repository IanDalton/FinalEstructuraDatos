
ids_municipios = {'Cordoba': ('CBA', 'AR-X'), 'Santa Fe': ('SFE', 'AR-S'), 'Tucuman': ('TUC', 'AR-T'), 'Santa Cruz': ('SCR', 'AR-Z'),
 'Corrientes': ('COR', 'AR-W'), 'Mendoza': ('MZA', 'AR-M'), 'Buenos Aires': ('BUE', 'AR-B'), 'Entre Rios': ('ERI', 'AR-E'), 'Misiones': ('MIS', 'AR-N'),
  'Chubut': ('CHU', 'AR-U'), 'Chaco': ('CHA', 'AR-H'), 'La Pampa': ('LPA', 'AR-L'), 'Rio Negro': ('RNO', 'AR-R'), 'San Juan': ('SJU', 'AR-J'), 
  'Jujuy': ('JUJ', 'AR-Y'), 'Salta': ('SAL', 'AR-A'), 'La Rioja': ('LRJ', 'AR-F'), 'Catamarca': ('CAT', 'AR-K'), 
  'Tierra del Fuego': ('TDF', 'AR-V'), 'Neuquen': ('NEU', 'AR-Q'), 'Ciudad Autonoma de Buenos Aires': ('CAB', 'AR-C'), 'Santiago del Estero': ('SGO', 'AR-G'), 
  'San Luis': ('SLU', 'AR-D'), 'Formosa': ('FOR', 'AR-P')}

def verificador_municipios(dict):
    return dict["municipio_id"][:3] == ids_municipios[dict["provincia"]][0]

