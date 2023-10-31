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