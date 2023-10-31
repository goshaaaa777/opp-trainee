nombre_fichero = 'Archivos_y_Exepciones/ejercicio/ejercicios/ficheros/ficheros/contar_palabras.txt'

with open(nombre_fichero) as fichero_abierto:
    contenido = fichero_abierto.read()
    contenido_parseado = contenido.replace('\n','')
    lista_palabras = contenido_parseado.split(' ')
    longitud_palabras = len(lista_palabras)
    print(longitud_palabras)


nombre_fichero = 'Archivos_y_Exepciones/ejercicio/ejercicios/ficheros/ficheros/palabras_repetidas.txt'

with open(nombre_fichero) as fichero_abierto:
    contenido = fichero_abierto.read()
    contenido_parseado = contenido.replace('\n','')
    lista_palabras = contenido_parseado.split(' ')
    numero_palabras = lista_palabras.count('palabras')
    print(longitud_palabras)
    contenido_sin_repetir = contenido.replace('palabras',' ')

nombre_fichero_destino = 'Archivos_y_Exepciones/ejercicio/ejercicios/ficheros/ficheros/palabras_sin_repetir.txt'

with open(nombre_fichero_destino, 'w') as fichero_abierto:
    fichero_abierto.write(contenido_sin_repetir)

