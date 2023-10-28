################### EJERCICIOS DE FUNCIONES #####################

################### EJERCICIO 1 #####################

# 1.Crea una función llamada "calcular_impuestos" que reciba dos argumentos: "ingresos" (int) y "tasa_impuestos" (float) y retorne los impuestos a pagar (float)
#   (por ejemplo: calcular_impuestos(50000, 0.25))
# 2.Dentro de la función, calcula el impuesto debido multiplicando los ingresos por la tasa de impuestos y guarda el resultado en una variable "impuesto_debido".
# 3.Retorna el valor de "impuesto_debido".
# 4.Crea una variable "ingresos" con el valor de tus ingresos anuales (por ejemplo: 75000)
# 5.Crea una variable "tasa_impuestos" con el porcentaje de impuestos que debes pagar (por ejemplo: 0.3)
# 6.Crea una variable "impuesto_a_pagar" que sea igual a la función "calcular_impuestos" con los argumentos "ingresos" y "tasa_impuestos".
# 7.Imprime "Impuesto a pagar: " y el valor de "impuesto_a_pagar".

def calcular_impuestos(ingresos : int, tasa_impuestos : float) -> float:
    impuesto_debido : float = ingresos * tasa_impuestos
    return impuesto_debido

ingresos : int = 75000
tasa_impuesto : float = 0.3

impuesto_a_pagar : float = calcular_impuestos(ingresos, tasa_impuesto)
print(f"Tasa de impuesto a pagar {tasa_impuesto} y el valor de los impuestos es {impuesto_a_pagar}" )

################### EJERCICIO 2 #####################

# 1.Crea una función llamada "calcular_promedio" que reciba una lista de números como argumento llamada "numeros" y retorne el promedio (float).
# 2.Dentro de la función, calcula el promedio de los números en la lista y guarda el resultado en una variable "promedio".
# 3.Retorna el valor de "promedio".
# 4.Crea una lista de números con las calificaciones obtenidas en un curso (por ejemplo: [9, 8, 10, 7, 8, 9, 6, 8, 10, 9])
# 5.Llama a la función "calcular_promedio" con la lista de calificaciones como argumento y guarda el resultado en una variable "promedio_curso"
# 6.Imprime "El promedio del curso es: " y el valor de "promedio_curso"

def calcular_promedio(numeros:list) ->float:
    numeros_acumulados : float = 0
    for numero in numeros:
        numeros_acumulados = numeros_acumulados + numero
    promedio : float = numeros_acumulados / len(numeros)
    return promedio

calificaciones : list = [9, 8, 10, 7, 8, 9, 6, 8, 10, 9]
promedio_curso : float = calcular_promedio(calificaciones)

print(f"El promedio de notas de tu curso es {promedio_curso}")

################### EJERCICIO 3 #####################

# 1.Crea una función llamada "calcular_costo_envio" que reciba dos argumentos: "origen" (str) y "destino" (str) y retorne el precio (int) 
#   (por ejemplo: calcular_costo_envio("Nueva York", "Los Ángeles"))
# 2.Dentro de la función, crea un diccionario con los costos de envio entre diferentes ciudades 
#   (por ejemplo: {"Nueva York": {"Los Ángeles": 20, "Chicago": 10, "Miami": 15}, "Los Ángeles": {"Nueva York": 25, "Chicago": 17, "Miami": 20}})
# 3.Usa los argumentos "origen" y "destino" para obtener el costo de envio entre esas dos ciudades del diccionario y guarda el resultado en una variable "costo"
# 4.Retorna el valor de "costo"
# 5.Crea una variable "origen" con el lugar de origen del envio (por ejemplo: "Nueva York")
# 6.Crea una variable "destino" con el lugar de destino del envio (por ejemplo: "Los Ángeles")
# 7.Llama a la función "calcular_costo_envio" con las variables "origen" y "destino" como argumentos y guarda el resultado en una variable "costo_envio"
# 8.Imprime "El costo de envio desde " + origen + " hasta " + destino + " es de: " + costo_envio


def calcular_costo_envio(origin :str, destino: str) -> int:
    costos_envio: dict = {"Nueva York": {"Los Ángeles": 20, "Chicago": 10, "Miami": 15}, "Los Ángeles": {"Nueva York": 25, "Chicago": 17, "Miami": 20}}
    informacion_destino : dict = costos_envio[origin]
    costo_destino : int = informacion_destino.get(destino, -1)
    return costo_destino

origen : str = "Nueva York"
destino : str ="Los Ángeles"

costo_envio : int = calcular_costo_envio(origen, destino)
print(f"El costo de envio desde {origen} hasta {destino} es de {costo_envio} dolares")

################### EJERCICIO 4 #####################

# 1.Crea una función llamada "convertir_moneda" que convierta dolares a otra moneda. 
#   La función recibe como argumento "cantidad_dolares" (int) y otro argumento opcional "moneda_destino" donde moneda_destino tiene como valor por defecto "euros", 
#   retorna un valor tipo float.
# 2. Dentro de la funcion crear un diccionario llamado "tasas_cambio" con estos valores: 'euros': 0.91, 'yenes': 106.23, 'libras': 0.77.
# 3. Crea una variable llamada "cantidad_destino" que guarde el valor de "cantidad_dolares" convertida a la moneda destino. Retorna "cantidad_destino"
# 4. Crea una variable llamada "dolares" con una cantidad; por ejemplo 1000.
# 5. Llama a la función "convertir_moneda" con "dolares" y "yenes" como parámetros y guarda el resultado en una variable llamada "yenes".
# 6. Imprime el valor de la variable "yenes".

def convertir_moneda(cantidad : int, moneda_destino : str ="Euros") -> float:
    tasas_cambios : dict = {'euros': 0.91, 'yenes': 106.23, 'libras': 0.77, 'dolares':1.00}
    cantidad_desitno : float = cantidad * tasas_cambios[moneda_destino]
    return cantidad_desitno

dolares : int = 1000
yenes = convertir_moneda(dolares, "yenes")
print(yenes)
################### EJERCICIO 5 #####################

# 1.Crea una función llamada "aplicar_descuento" para comprar un producto en distintas divisas y con posibles descuentos,
#   que reciba como argumentos "producto" (str), "moneda" (str) como argumento opcional y argumentos **kwargs con productos como key y value siendo un diccionario con el precio 
#   del producto y el descuento a aplicar. 
#   (Ejemplo de uso de la función -> aplicar_descuento('zapatos','euros',zapatos={"precio": 12.99, "descuento": 0.1},
    # collar={"precio": 9.99, "descuento": 0.2},
    # pulsera={"precio": 19.99, "descuento": 0.15},
    # gafas={"precio": 29.99, "descuento": 0.25})
# 2.La función debe calcular el precio final en base a los argumentos recibidos. Si se especifica un descuento, debe aplicarlo al precio. 
# 3.Si se especifica una moneda diferente a la predeterminada, debe convertir el precio al valor en la moneda especificada, 
#   con la función realizada en el Ejercicio 6 llamada "convertir_moneda".
# 5.Usa la función "aplicar_descuento" para calcular el precio final de varios productos con diferentes argumentos opcionales.
# 6.Asegúrate de manejar el caso en el que no se pase ningún parámetro key-value.

def aplicar_descuento(producto: str, moneda: str = 'dolares', **kwargs) -> float:
    if kwargs and producto in kwargs.keys():
        precio : float = kwargs[producto]['precio']
        descuento : float = kwargs[producto]['descuento']
        precio_con_cambio : float = convertir_moneda(precio, moneda)
        precio_con_descuento : float = precio_con_cambio - (precio_con_cambio * descuento )
        return precio_con_descuento
    return -1

precio_final : float = aplicar_descuento('zapatos','euros',zapatos={"precio": 12.99, "descuento": 0.1},
    collar={"precio": 9.99, "descuento": 0.2},
    pulsera={"precio": 19.99, "descuento": 0.15},
    gafas={"precio": 29.99, "descuento": 0.25})

print(precio_final)