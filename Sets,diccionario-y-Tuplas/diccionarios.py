## Creacion y acceso de diccionarios

# Diccionario vacio inicializado con disct()
diccionario = dict()
# Diccionario vacio inicializado con llaves
diccionario = {}
# Diccionario inicilizado con valores
tecnologia = {'Web':{'JavaScript', 'Html', 'Css'}, 'Videojuegos':{'Unity','C#'}}
print(tecnologia)
## Inserccion y actualizacion en diccionarios 
tecnologia['Data Engineer'] = ['Python','Hadoop']
tecnologia.update({'Desarrollo Movil': ['Android','IOS']})
## Borrados de elementos en diccionarios

valor_borrado = tecnologia.pop('Web')
mensaje_borrado = tecnologia.pop("Ciberseguridad","No existe ciberseguridad")
ultimo_elemnto = tecnologia.popitem()
tecnologia.clear()

## Otros metodos
tecnologia = {'Web':{'JavaScript', 'Html', 'Css'}, 'Videojuegos':{'Unity','C#'}}
bkp_superficial = tecnologia.copy()
import copy
copia_profunda = copy.deepcopy(tecnologia)
print(bkp_superficial)
## Acceso a elementos en diccionarios 
tecnologia_web = tecnologia.get('web')
print(tecnologia_web)
claves = tecnologia.keys()
items = tecnologia.items()
print(items)
# Recorrido de un diccionario

for key,value in tecnologia.items():
    print(f"La clase de este elento es: {key} y el valor es: {value}")    