from Modulos.clases import *
from Modulos.verificador import ids_municipios
arg = Pais('Argentina',84560000)

for key,value in ids_municipios.items():
    Provincia(key,arg,value[1])

arg.save_error(arg.load_data('I:\Github\FinalEstructuraDatos\Datos\municipios.csv','Municipio'),'municipios')
arg.save_error(arg.load_data('I:\\Github\\FinalEstructuraDatos\\Datos\\routers.csv','Router'),'routers')


