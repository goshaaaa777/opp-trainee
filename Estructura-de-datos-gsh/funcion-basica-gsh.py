def mi_funcion(num1, num2):
    resultado = num1 + num2
    print(resultado)

    if resultado > 100:
        print("El num es mayor que 100")
    else:
        print("El num es menor que 100")

mi_funcion(20,30)

def generador_de_saludos(nombre):
    print(f'hola {nombre}')

generador_de_saludos('Fernanda')
generador_de_saludos('Isaias')