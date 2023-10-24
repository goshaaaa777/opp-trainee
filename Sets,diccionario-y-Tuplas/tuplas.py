## Creacion de tuplas ##

tupla_vacia = ()
tupla_uno = ('Arturo','Lorenzo','Gosha')
tupla_dos = ('r2d2','coder')

## Insertar y actualizar ##
#Las tuplas no cuentan con mètodos de insercion y actualizacion puesto que son inmutables, una vez creadas no se pueden cambiar.

## Borrados ##
del tupla_vacia

## Operaciones de tuplas ##
tuplas_tres = tupla_uno + tupla_dos
index_gosha = tupla_uno.index('Gosha')
print(index_gosha)

count_coder = tupla_dos.count('coder')
#Acceso de forma indexada

print(tupla_uno[0])

#Acceso con intervalos de elementos

print(tupla_uno[0:2])

#Acceso de bucles for

for palabra in tupla_uno:
    print(palabra)
