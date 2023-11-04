
""" numero = 30

if numero < 10:
    print(f"El numero que has ingresado {numero} es menor")
elif numero == 10:
    print(f"El numero que has ingresado {numero} es igual al que tenemos en el sistema")
else:
    print(f"El numero que has ingresado {numero} es mayor al que tenemos en el sistema")

dinero = int(input("Introduzca su Dinero en dolares:\n"))

respuesta = None

if dinero >= 1000:
    print("Usted es millonario, puede pedir un prestamo.")
    respuesta = input("1-Carro.\n2-Casa.\n3-Negocio\n4-Viajes\n5-Prestamo\n")

    if respuesta == "1":
        print("Ha elegido un prestamos para comprar un Carro.")
    elif respuesta == "2":
        print("Ha elegido un prestamos para comprar un Casa.")
    elif respuesta == "3":
        print("Ha elegido un prestamos para comprar un Negocio.")
    elif respuesta == "4":
        print("Ha elegido un prestamos para comprar un Viaje.")
    elif respuesta == "5":
        print("Ha elegido un prestamo.")
    else:
        print("Opciòn no valida.")
else:
    print("Usted no tiene el dinero suficiente para solicitar un prestamo")
    

respuesta = input("1-Suma.\n2-Resta.\n3-Multiplicacion\n4-Division\n5-Modulo\n6-Exponente\n")
"""

eleccion = int(input("Introduzca su Dinero en dolares:\n"))
error = True


match eleccion:
    case 1:
        print('Ha elegido la opcion "Suma".')
    case 2:
        print('Ha elegido la opcion "Resta".')
    case 3:
        print('Ha elegido la opcion "Multiplicacion".')
    case 4:
        print('Ha elegido la opcion "Division".')
    case 5:
        print('Ha elegido la opcion "Modulo".')
    case 6:
        print('Ha elegido la opcion "Exponente".')
    case _:
        print('ERROR, Opcion invalida')
        error = False

if error:
    numero_1 = float(input("Especifique el primero operador:\n"))
    numero_2 = float(input("Especifique el segundo operador:\n"))

    match eleccion:
        case 1:
            resultado = round(numero_1 + numero_2, 2)
            print(f"El numero de suma {numero_1} + {numero_2} = {resultado}")
        case 2:
            resultado = round(numero_1 - numero_2, 2)
            print(f"El numero de suma {numero_1} - {numero_2} = {resultado}")
        case 3:
            resultado = round(numero_1 * numero_2, 2)
            print(f"El numero de suma {numero_1} por {numero_2} = {resultado}")
        case 4:
            resultado = round(numero_1 / numero_2, 2)
            print(f"El resultado de dividir {numero_1} entre {numero_2} = {resultado}")
        case 5:
            resultado = round(numero_1 % numero_2, 2)
            print(f"El resto de la division de {numero_1} entre {numero_2} = {resultado}")
        case 6:
            resultado = round(numero_1 ** numero_2, 2)
            print(f"{numero_1} elevado a {numero_2} es= {resultado}")
else:
    print("Por favor, vuelva a ejecutar la calculadora.")