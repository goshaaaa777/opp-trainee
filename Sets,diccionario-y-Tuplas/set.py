## Set Vacio
nuevo_set : set()

## Inicialiazr u set con elementos
nuevo_set = {"uno","dos"}

##
nuevo_set.add('tres')
nuevo_set.update({"tres","cuatro"})
print(nuevo_set)



nuevo_set.discard('cinco')
nuevo_set.remove('uno')
nuevo_set.clear()

print(nuevo_set)


set_uno = {1,2,3,4,5}
set_dos = {5,6,7,8}

set_diferencia = set_uno.difference(set_dos)
set_diferencia_simetrica = set_uno.symmetric_difference(set_dos)
set_interseccion = set_uno.intersection(set_dos)
set_interseccion = set_uno.union(set_dos)
print(set_uno)

no_tiene_intersaccion = set_uno.isdisjoint(set_dos)
es_subconjunto = set_dos.issubset(set_uno)

print(set_diferencia_simetrica)