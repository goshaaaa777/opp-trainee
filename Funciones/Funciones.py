# Sintaxis: def nombre_funcion(parametro1 : Tipo1, parametro2: Tipo2) -> TipoDatoRetorno:
#               Acciones
#               return Valor (Opcional)

############################# FUNCIÓN SIN PARÁMETROS #####################################

def funcion_basica() -> None:
    print("Soy una funcion basica")
funcion_basica()


############################# FUNCIÓN CON PARÁMETROS #####################################

# Python es un lenguaje con tipado dinámico, es decir, no hace falta indicar que tipo de datos va a recibir o devolver una función ya que Python
# va a inferir los tipo de datos en tiempo de ejecución. Es muy recomendable indicar los tipos de datos para aumentar la legibilidad del código.
# Es más, aunque tu le indiques el tipo de parámetros y luego le pasas otro tipo de datos NO va a dar un fallo.

def suma(numero1: int, numero2:int) -> int:
    resultado: int = numero1 + numero2
    return resultado

resultado : int = suma(100, 400)
print(resultado)

############################# FUNCIÓN CON PARÁMETROS CON VALORES POR DEFECTO #####################################

def sacar_dinero(saldo_cuenta : int, dinero_a_retirar : int = 20):
    return saldo_cuenta - dinero_a_retirar

saldo : int = 5000
saldo_restante : int = sacar_dinero(saldo)
print(saldo_restante)
print(f"Su saldo restante es {saldo_restante}")

############################# FUNCIÓN CON PARÁMETROS OPCIONALES #####################################

# En los parametros opcionales no hace falta definir que tipo de datos tienen porque internamente python los va a meter en tuplas. Los toppings que
# le pasemos en la función van a ser metidos en una tupla internamente.

def crear_pizza(tipo_pizza: str, *toppings_ext) -> str:
    tipos_pizza : list = ['Margarita','Cuatro Quesos','Barbacoa']
    frase_respuesta : str = ""

    if tipo_pizza in tipos_pizza and not toppings_ext:
        frase_respuesta = f"Tu pizza {tipo_pizza} se esta procesando, vuelve en 10 minutos. No tiene toppings"
    elif tipo_pizza in tipos_pizza and toppings_ext:
        frase_respuesta = f"Tu pizza {tipo_pizza} con los toppings {str(toppings_ext)} se esta procesando, vuelve en 10 minutos"
    else:
        frase_respuesta = f"Tu tipo de pizza {tipo_pizza} no està en nuestro menù, lo sentimos mucho"
    return frase_respuesta

respuesta : str = crear_pizza('Margarita')
respuesta1 : str = crear_pizza('Barbacoa','Salchicha')
print(respuesta1)

############################# FUNCIÓN CON PARÁMETROS KEY-VALUE #####################################

# Sirve para cuando necesitamos un número variable de parámetros que tengan forma de diccionario, el nombre kwargs se pone por convención del lenguaje.
# En este caso queremos crear un perfil de usuario que tenga como obligatorio poner el nombre y apellidos y la demás información de forma opcional.


def crear_perfil_usuario(nombre : str, apellidos :str, **kwargs) -> str:
    perfil : str = f"****** INFORMACIÒN DEL USUARIO {nombre} {apellidos} ******"
    for key,value in kwargs.items():
        perfil = f"{perfil} \n {key} : {value}"
    return perfil

perfil1 : str = crear_perfil_usuario('Isaias','Capistrano Huamani')
perfil2 : str = crear_perfil_usuario('Isaias','Capistrano Huamani', Ciudad='Callao',Pais='Perù', Comida_favorita='Ceviche')

print(perfil2)
############################# FUNCIÓNES QUE TIENEN COMO PARÁMETROS FUNCIONES #####################################

# Todo en Python son objetos hasta las funciones por eso podemos pasar una función como parámetro a otra función.
# En este ejemplo hacemos una función que reciba que tipo de operación tiene que hacer sobre dos números, está operación se define como una función.

def dos_elementos(lista:list) -> str:
    if len(lista) >= 2:
        return lista[0], lista[1]
    return "",""

nombres : list = ['Juan','Pepe','Jorge']
nombre1, nombre2 = dos_elementos(nombres)

############################# FUNCIÓNES QUE DEVUELVE MÁS DE UN VALOR #####################################




############################# ORDEN DE PARÁMETROS #####################################

# Orden de posicionamiento de los parámetros según el tipo:
# 1. Parametros obligatorios
# 2. Parametros opcionales
# 3. Parametros key-value.
#        def funcion(parametros_obligatorios, *parametros_opcionales, **kwargs_arguments)
