#Lista Vacia
lista_vacia : list = []
lista_vacia : list = list()

#Lista con elementos
motocicletas = ['honda','yamaha','suzuki','bmw','honda']

#Inserciones y actualizaciones
motocicletas.append('audi')
motocicletas.insert(0, 'daelin')
motocicletas[1] = 'bmw'

#Borrados
"""otocicletas.clear()
elemento_cero = motocicletas.pop(0)
"""

#Sort
"""
numeros = ['1','2','5','4','6','3']
numeros.sort(reverse=True)
print(numeros) """

##### Accesos a las listas #####
# La forma de acceder a los elementos de una listaes con el operador [inicio:fin] indicando el inicio de elementos que quieres de la lista
# y fin indica el elemento - 1 que va recoger de la lista. Los indices empiezan en 0

numero = [2,3,1,5,5]
primer_elemento = numero[0]
primeros_elemento = numero[0:2]
ultimo_elemento = numero[-1]
ultimos_elemento = numero[-3:]

# Tambièn podemos indicar cada X nùmero de elementos coger un elemento. Con un tercer separador lista[inicio:fin:numero_saltos]. Si numero_saltos
# es positivo entonces empezamos desde el principio de la lista hasta el final, si numero_saltos es negativo empezemos desde el final hasta el princio

todos_elementos = numero[::1] 
numeros_impares = numero[::2]
lista_reversa = numero[::-1]

comidas_no_sanas = ['pizza','tacos','tortas','tacos']
comidas_sanas = ['ensalada de verduras','ensalada de frutas']

comidas = comidas_no_sanas + comidas_sanas
comidas_no_sanas.extend(comidas_sanas)
print(comidas)