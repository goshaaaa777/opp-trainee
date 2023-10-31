ruta_no_existe = 'fichero_no_existe.txt'

try:
     with open(ruta_no_existe) as fichero_abierto:
        contenido = fichero_abierto.read()
except FileNotFoundError:
    print(f'El fichero {ruta_no_existe} no existe.')

print("Hola Mundo")


class ValorDemasLadoPequeno(Exception):
    pass

class ValorDemasiadoGrande(Exception):
    pass


def valor_numero(numero_usuario : int) -> bool:
    if numero_usuario < numero_deseado:
        raise ValorDemasLadoPequeno("El numero que has puesto es menor")
    elif numero_usuario > numero_deseado:
        raise ValorDemasiadoGrande("El numero que has puesto es mayor")
    else:
        print("Enhorabuena acertaste el numero!")
        
    
numero_deseado = 0

while True:
    numero_usuario = int(input("Adivina un numero entre el 1 al 10"))
    try:
        valor_numero(numero_usuario)
    except ValorDemasLadoPequeno:
        print("El numero que has puesto es menor")        
    except ValorDemasiadoGrande:
        print("El numero que has puesto es mayor")


    