nombre_ficheros = "./Archivos-y-Exepciones/pi_digits.txt"

with open(nombre_ficheros) as fichero_abierto:
    contenido = str = fichero_abierto.read()
    print(contenido)

with open(nombre_ficheros) as fichero_abierto:
    for linea in fichero_abierto:
        print(linea)

with open(nombre_ficheros) as ficherop_abierto:
    lineas = fichero_abierto.readline()
    print(lineas)

nombre_fichero = './Archivos-y-Exepciones/test.txt'

with open(nombre_fichero, 'w') as fichero_nuevo:
    fichero_nuevo.write('pruba ficheros')