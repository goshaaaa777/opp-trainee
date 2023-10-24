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

def sacar_dinero(cuenta_bancaria : int, dinero_a_retirar : int = 20):
    return cuenta_bancaria - dinero_a_retirar


############################# FUNCIÓN CON PARÁMETROS OPCIONALES #####################################

# En los parametros opcionales no hace falta definir que tipo de datos tienen porque internamente python los va a meter en tuplas. Los toppings que
# le pasemos en la función van a ser metidos en una tupla internamente.



# Salchicha y pimiento rojo son parámetros opcionales.



############################# FUNCIÓN CON PARÁMETROS KEY-VALUE #####################################

# Sirve para cuando necesitamos un número variable de parámetros que tengan forma de diccionario, el nombre kwargs se pone por convención del lenguaje.
# En este caso queremos crear un perfil de usuario que tenga como obligatorio poner el nombre y apellidos y la demás información de forma opcional.




############################# FUNCIÓNES QUE TIENEN COMO PARÁMETROS FUNCIONES #####################################

# Todo en Python son objetos hasta las funciones por eso podemos pasar una función como parámetro a otra función.
# En este ejemplo hacemos una función que reciba que tipo de operación tiene que hacer sobre dos números, está operación se define como una función.




############################# FUNCIÓNES QUE DEVUELVE MÁS DE UN VALOR #####################################




############################# ORDEN DE PARÁMETROS #####################################

# Orden de posicionamiento de los parámetros según el tipo:
# 1. Parametros obligatorios
# 2. Parametros opcionales
# 3. Parametros key-value.
#        def funcion(parametros_obligatorios, *parametros_opcionales, **kwargs_arguments)
